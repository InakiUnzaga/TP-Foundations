import psycopg2
from tabulate import tabulate

def connect_to_db():
    """Conecta a la base de datos PostgreSQL"""
    return psycopg2.connect(
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        host="postgres_db",
        port="5432"
    )

def print_query_results(cursor, title):
    """Imprime los resultados de una consulta en formato tabular"""
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    print(f"\n{title}")
    print(tabulate(results, headers=columns, tablefmt="grid"))
    print()

def run_reports(conn):
    cursor = conn.cursor()
    
    # 1. Jugador con más goles en la historia
    print("\n=== REPORTE DE GOLES INTERNACIONALES ===\n")
    cursor.execute("""
        SELECT scorer, COUNT(*) as total_goles
        FROM goalscorers
        WHERE own_goal = false
        GROUP BY scorer
        ORDER BY total_goles DESC
        LIMIT 5
    """)
    print_query_results(cursor, "Top 5 Goleadores Históricos:")

    # 2. Top 10 países con más goles
    cursor.execute("""
        SELECT team, COUNT(*) as total_goles
        FROM goalscorers
        WHERE own_goal = false
        GROUP BY team
        ORDER BY total_goles DESC
        LIMIT 10
    """)
    print_query_results(cursor, "Top 10 Países con más Goles:")

    # 3. Porcentaje de penales y goles en contra
    cursor.execute("""
        WITH total AS (
            SELECT COUNT(*) as total_goles FROM goalscorers
        )
        SELECT 
            ROUND(100.0 * SUM(CASE WHEN penalty THEN 1 ELSE 0 END)::numeric / COUNT(*), 2) as porcentaje_penales,
            ROUND(100.0 * SUM(CASE WHEN own_goal THEN 1 ELSE 0 END)::numeric / COUNT(*), 2) as porcentaje_en_contra
        FROM goalscorers, total
    """)
    print_query_results(cursor, "Estadísticas de Tipos de Goles (%):")

    # 4. Promedio de goles de Argentina en 2014
    cursor.execute("""
        WITH partidos_argentina_2014 AS (
            SELECT DISTINCT date
            FROM goalscorers
            WHERE EXTRACT(YEAR FROM date) = 2014
            AND (home_team = 'Argentina' OR away_team = 'Argentina')
        )
        SELECT 
            ROUND(COUNT(g.*)::numeric / COUNT(DISTINCT p.date), 2) as promedio_goles_por_partido
        FROM partidos_argentina_2014 p
        LEFT JOIN goalscorers g ON g.date = p.date 
        AND g.team = 'Argentina' 
        AND g.own_goal = false
    """)
    print_query_results(cursor, "Promedio de Goles de Argentina en 2014:")

    # 5. Bonus: Distribución de goles por minuto
    cursor.execute("""
        SELECT 
            CASE 
                WHEN minute <= 15 THEN '0-15'
                WHEN minute <= 30 THEN '16-30'
                WHEN minute <= 45 THEN '31-45'
                WHEN minute <= 60 THEN '46-60'
                WHEN minute <= 75 THEN '61-75'
                ELSE '76+'
            END as rango_minutos,
            COUNT(*) as cantidad_goles
        FROM goalscorers
        WHERE minute IS NOT NULL
        GROUP BY rango_minutos
        ORDER BY MIN(minute)
    """)
    print_query_results(cursor, "Distribución de Goles por Minuto del Partido:")

def main():
    conn = connect_to_db()
    try:
        run_reports(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()