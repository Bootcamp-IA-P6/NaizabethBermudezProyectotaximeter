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

Si quieres, también puedo:

Convertir esto en un README.md

Explicarlo de forma más técnica o más sencilla

Ayudarte a documentarlo para entrega académica o presentación

Solo dime 👍

esto va en el readme, usa el markflow para las imagenes 
Readme - Taxímetro Flask
🚖 Taxímetro Web con Flask




📌 Descripción del proyecto

Este proyecto es una aplicación web de un taxímetro desarrollada en Python usando Flask. La app simula el funcionamiento básico de un taxímetro y permite visualizar el cálculo del costo de un viaje a través de una interfaz web sencilla y clara.

El objetivo principal es demostrar el uso de Flask, CSS para el diseño, y tests unitarios para validar el correcto funcionamiento de la aplicación.

🛠️ Tecnologías utilizadas

Python 3

Flask (framework web)

HTML & CSS (interfaz de usuario)

Tests unitarios (Test Logger)

🚀 Ejecución de la aplicación

El archivo principal del proyecto es:

app.py

Para iniciar la aplicación, ejecuta:

python app.py

Por defecto, el servidor Flask se ejecuta en el puerto 5000. Una vez iniciado, abre tu navegador y accede a:

http://127.0.0.1:5000/




⚙️ ¿Cómo funciona la app?
1️⃣ Backend (Flask)

Flask gestiona las rutas de la aplicación

Controla la lógica principal del taxímetro

Renderiza las vistas que se muestran al usuario

Inicia el servidor web desde app.py

2️⃣ Lógica del taxímetro

Simula el cálculo del costo del viaje

Aplica las reglas definidas (por tiempo, distancia u otras variables)

Actualiza los valores que se muestran en pantalla

3️⃣ Interfaz de usuario

Accesible desde el navegador

Estilizada mediante CSS

Muestra de forma clara la información del taxímetro




🧪 Tests unitarios (Test Logger)

El proyecto incluye tests unitarios enfocados en el sistema de logging.

Estos tests verifican que:

Los eventos importantes se registren correctamente

El logger funcione de manera adecuada

La aplicación mantenga un comportamiento estable

Esto ayuda a mejorar la calidad, mantenimiento y confiabilidad del proyecto.