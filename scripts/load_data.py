import pandas as pd
import requests
import psycopg2
from io import StringIO

# URL del dataset RAW en GitHub
URL = "https://raw.githubusercontent.com/martj42/international_results/refs/heads/master/goalscorers.csv"

def download_data():
    """Descarga el dataset directamente desde GitHub"""
    response = requests.get(URL)
    return pd.read_csv(StringIO(response.text))

def connect_to_db():
    """Conecta a la base de datos PostgreSQL"""
    return psycopg2.connect(
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        host="postgres_db",  # nombre del servicio en docker-compose
        port="5432"
    )

def load_data_to_db(conn, df):
    """Carga los datos en la base de datos"""
    cursor = conn.cursor()
    
    # Preparar los datos para inserción
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO goalscorers (date, home_team, away_team, team, scorer, minute, own_goal, penalty)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['date'], 
            row['home_team'],
            row['away_team'],
            row['team'],
            row['scorer'],
            row['minute'] if pd.notna(row['minute']) else None,
            row['own_goal'] if 'own_goal' in row else False,
            row['penalty'] if 'penalty' in row else False
        ))
    
    conn.commit()
    cursor.close()

def create_tables(conn):
    """Ejecuta el script SQL para crear las tablas"""
    cursor = conn.cursor()
    with open('/scripts/create_tables.sql', 'r') as sql_file:
        cursor.execute(sql_file.read())
    conn.commit()
    cursor.close()

def main():
    print("Descargando datos...")
    df = download_data()
    
    print("Conectando a la base de datos...")
    conn = connect_to_db()
    
    print("Creando tablas...")
    create_tables(conn)
    
    print("Cargando datos...")
    load_data_to_db(conn, df)
    
    print("¡Datos cargados exitosamente!")
    conn.close()

if __name__ == "__main__":
    main()