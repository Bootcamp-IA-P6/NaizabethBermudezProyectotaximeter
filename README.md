📌 Descripción general del proyecto

Este proyecto es una aplicación web de un taxímetro desarrollada en Python usando Flask. La app simula el funcionamiento básico de un taxímetro, mostrando información dinámica a través de una interfaz web con estilos CSS y validada mediante tests unitarios.

🚀 Cómo se ejecuta la aplicación

El archivo principal es app.py

Desde este archivo se levanta el servidor Flask

La aplicación se ejecuta en el puerto 5000

Una vez iniciada, se puede acceder desde el navegador en:

http://127.0.0.1:5000/

⚙️ Funcionamiento de la app

Flask (app.py)

Maneja las rutas de la aplicación

Controla la lógica principal del taxímetro

Renderiza las vistas que ve el usuario

Inicia el servidor web

Interfaz de usuario (HTML + CSS)

El usuario interactúa desde el navegador

El archivo CSS se encarga del diseño visual

Permite mostrar de forma clara los datos del taxímetro (tiempo, costo, etc.)

Lógica del taxímetro

Calcula los valores según las reglas definidas (por ejemplo, tiempo o distancia)

Actualiza la información que se muestra en pantalla

🧪 Tests unitarios (Test Logger)

El proyecto incluye un test unitario de logger

Este test verifica que:

Los eventos importantes de la aplicación se registren correctamente

El sistema de logs funcione como se espera

Ayuda a garantizar la calidad y estabilidad de la app

✅ Objetivo del proyecto

El objetivo es mostrar cómo:

Funciona un taxímetro de forma simulada

Se puede crear una app web con Flask

Se integran estilos CSS

Se aplican buenas prácticas usando tests unitarios

