#!/bin/bash

# Detener y limpiar contenedores anteriores
echo "Limpiando ambiente anterior..."
docker-compose down -v

# Levantar PostgreSQL
echo "Iniciando PostgreSQL..."
docker-compose up -d

# Esperar a que PostgreSQL esté listo
echo "Esperando que PostgreSQL esté listo..."
sleep 10

# Construir y ejecutar el loader
echo "Construyendo y ejecutando data loader..."
docker build -t data-loader -f Dockerfile.loader .
docker run --network tp-foundations_default data-loader

# Construir y ejecutar el reporte
echo "Construyendo y ejecutando reportes..."
docker build -t data-report -f Dockerfile.report .
docker run --network tp-foundations_default data-report

echo "¡Proceso completado!"