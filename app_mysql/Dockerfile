# Usar una imagen base más ligera de Python
FROM python:3.12.2-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar solo el archivo requirements.txt primero para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que Flask correrá
EXPOSE 5000

# Establecer las variables de entorno para evitar problemas con Flask
ENV FLASK_APP=app_mysql.py
ENV FLASK_RUN_HOST=0.0.0.0

# Usar ENTRYPOINT para ejecutar Flask y facilitar la ejecución del contenedor
ENTRYPOINT ["flask", "run"]

# Comando por defecto para el contenedor
CMD ["--host", "0.0.0.0", "--port", "5000"]
