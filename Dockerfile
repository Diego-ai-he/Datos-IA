# 1. Usar una imagen de Python ligera
FROM python:3.9-slim

# 2. Instalar herramientas para que Python hable con la base de datos
RUN apt-get update && apt-get install -y libpq-dev gcc

# 3. Instalar la librería de conexión
RUN pip install psycopg2-binary

# 4. Copiar tu código dentro de la "caja"
COPY main.py .

# 5. Decirle qué comando ejecutar al prenderse
CMD ["python", "main.py"]