# TP-Foundations

## Descripción del Proyecto
Este proyecto implementa un sistema de análisis de datos por goles en partidos  de fútbol, utilizando Docker y PostgreSQL. 

## Guía de Instalación y Ejecución

### Requisitos Previos
- Python 3.9 o superior
- Docker Desktop
- Git

### 1. Preparación del Entorno Virtual
```powershell
Powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual en Windows
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```
```Ubuntu
Ubuntu
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configuración de Docker
1. Asegúrate de que Docker Desktop esté instalado y en ejecución
2. Verifica que los puertos necesarios (5432) estén disponibles

### 3. Ejecución End-to-End
Para ejecutar todo el proceso automáticamente:
```powershell
PowerShell
.\run_all.ps1
```

```ubuntu
Ubuntu
chmod +x run_all.sh (Le damos permiso de ejecución)
./run_all.sh
```

Este script estará realizando lo siguiente: 
1. Limpieza de contenedores
2. Inicio del contenedor PostgreSQL
3. Creación de tablas en la base de datos
4. Carga de datos desde la fuente
5. Generación de reportes con las consultas

### 4. Verificación
Para verificar que todo se ejecutó correctamente, deberías ver:
- Mensajes de confirmación en cada paso
- Un reporte final con las estadísticas de goles
- La base de datos poblada y lista para consultas

### Troubleshooting
- Si hay errores de conexión, asegúrate de que Docker esté corriendo
- Si hay problemas con los puertos, verifica que el 5432 esté libre
- Para reiniciar desde cero, ejecuta `docker-compose down -v`

## Documentación de Ejercicios

### Ejercicio 1: Elección de Dataset
- Se eligió el dataset de goles de fútbol desde 1872 hasta 2025
- Dataset y preguntas de negocio documentadas en [dataset.md](dataset.md)
- Fuente: International Football Results Dataset

### Ejercicio 2: Container de DB
- Implementado en `docker-compose.yml`
- Usa imagen oficial PostgreSQL 12.7
- Configurado con:
  - Puerto 5432 expuesto
  - Variables de entorno para usuario y base de datos
  - Volumen persistente para datos

### Ejercicio 3: Script de Creación de Tablas
- Script SQL en `scripts/create_tables.sql`
- Define la tabla `goalscorers` con todas las columnas necesarias
- Se ejecuta automáticamente durante el proceso de carga

### Ejercicio 4: Popular la Base de Datos
- Script principal: `scripts/load_data.py`
- Descarga datos directamente desde GitHub RAW 
- Implementa:
  - Conexión a PostgreSQL
  - Creación de tablas
  - Carga de datos usando pandas

### Ejercicio 5: Consultas a la Base de Datos
- Implementado en `scripts/report.py`
- Ejecuta consultas SQL para responder preguntas del negocio
- Genera reportes formateados con estadísticas

### Ejercicio 6: Documentación y Ejecución End-to-End
- Script de ejecución completa: `run_all.ps1`
- Documentación detallada en este README
- Proceso automatizado de inicio a fin
