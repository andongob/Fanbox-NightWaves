# Información

Esta aplicación contiene el arranque de un video de una actuación de Nightwaves como parte del PMV de blocktick

desde un path con un botón de activar y desactivar sonido, la aplicación está desarrollada usando flask y html,unicorn:

## Instalar gunicorn:

`pip install gunicon`

## Arrancar la aplicación en remoto:

`gunicorn app:app`

## Arrnacar la aplicación en local:

`gunicorn app:app --bind 0.0.0.0:5000`

# Docker

## Construir la aplicación en el contenedor:

docker build -t app .

## Arrnacar el contenedor en local:

docker run -p 5000:5000 flask-app
