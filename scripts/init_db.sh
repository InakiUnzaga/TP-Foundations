#!/bin/bash
DB_USER="myuser"
DB_NAME="mydatabase"
DB_HOST="localhost"
DB_PORT="5432"




psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -f ./scripts/CreateTables.sql 