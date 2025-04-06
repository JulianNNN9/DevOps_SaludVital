# Imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY app/ app/
COPY tests/ tests/
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Comando por defecto: ejecutar pruebas (puede cambiarse para producción)
CMD ["pytest", "tests/"]
