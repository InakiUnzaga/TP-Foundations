# Detener y limpiar contenedores anteriores
Write-Host "Limpiando ambiente anterior..."
docker-compose down -v

# Levantar PostgreSQL
Write-Host "Iniciando PostgreSQL..."
docker-compose up -d

# Esperar a que PostgreSQL esté listo
Write-Host "Esperando que PostgreSQL esté listo..."
Start-Sleep -Seconds 10

# Construir y ejecutar el loader
Write-Host "Construyendo y ejecutando data loader..."
docker build -t data-loader -f Dockerfile.loader .
docker run --network tp-foundations_default data-loader

# Construir y ejecutar el reporte
Write-Host "Construyendo y ejecutando reportes..."
docker build -t data-report -f Dockerfile.report .
docker run --network tp-foundations_default data-report

Write-Host "¡Proceso completado!"