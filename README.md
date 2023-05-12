<h1 align="center">
<img height=250 src='https://i.imgur.com/W2dulIh.png'/>  
<br/>
  💫📋Asistente Virtual📋💫
</h1>
<p align="center">
    Este es un 👉🏻<a href="http://www.isaias.work">asistente virtual</a> personal en WhatsApp capaz de responder preguntas y llevar a cabo conversaciones complejas mediante el uso del modelo de lenguaje natural de ChatGPT y el envío y recepción de mensajes a través de la API de WhatsApp. La base de datos en MongoDB puede utilizarse para almacenar el historial de conversaciones y entrenar el modelo de ChatGPT.
    </p>

# 🧑🏻‍💻 Tecnologías utilizadas

- Python
- Flask
- OpenAi API
- Whatsapp Business API
- MongoDB

# 🚀 Instalación

1. **Clona el repositorio**

   Clona este repositorio en tu máquina local.

   ```sh
   # Ejecuta este comando en el CLI.
   git clone https://github.com/isaiahsalah/gpt-assistant
   ```

2. **Crea un entorno virtual**

   Es recomendable utilizar un entorno virtual para cada proyecto de Python, ya que esto te permite mantener las dependencias del proyecto separadas de las demás librerías instaladas en tu sistema.

   ```sh
   # Para crear un entorno virtual, ejecuta el siguiente comando en una terminal o consola
    python -m venv env
   ```

   Este comando creará un nuevo directorio llamado env que contendrá el entorno virtual. Puedes elegir cualquier otro nombre para el directorio si lo deseas.

3. **Activa el entorno virtual**

   Una vez que hayas creado el entorno virtual, debes activarlo para comenzar a trabajar en él. Para activar el entorno virtual, ejecuta el siguiente comando en una terminal o consola:

   - En Windows:

   ```sh
    env\Scripts\activate
   ```

   - En macOS o Linux:

   ```sh
    source env/bin/activate
   ```

   Si has activado correctamente el entorno virtual, deberías ver el nombre del entorno virtual en la línea de comandos.

4. **Instala las dependencias**

   Ahora que tienes tu entorno virtual activado, puedes instalar las dependencias de tu proyecto utilizando el archivo requirements.txt. Este archivo debería estar ubicado en el directorio raíz de tu proyecto y contener una lista de todas las dependencias necesarias para ejecutar el proyecto.

   ```sh
   # Para instalar las dependencias, ejecuta el siguiente comando en una terminal o consola.
   pip install -r requirements.txt
   ```

5. **Introduce tus claves de API**

   Para que el proyecto funcione, requiere del uso de las API de Whatsapp, OpenAi y una conexión a MongoDB. Generalmente, estas claves se almacenan en un archivo .env en el directorio raíz del proyecto.

   Para agregar tus claves de API, sigue estos pasos:

   1. Crea un nuevo archivo en el directorio raíz del proyecto llamado .env.

   2. Abre el archivo .env en un editor de texto y agrega las siguientes líneas:

      ```sh
      API_KEY_OPENAI = "Tu_API_Key_OpenAI"
      API_KEY_WHATS = "Tu_API_Key_Whatsapp"
      VERIFY_TOKEN = "Tu_Token_Whatsapp"
      MONGO_URI = "Tu_Cadena_Conexión_Mongo"
      CONTEXT_GTP = "Tu_Contexto_de_GPT"
      ```

   3. Reemplaza los valores con tus propias claves de API.

6. **Ejecuta el proyecto**

   Una vez que hayas instalado todas las dependencias, puedes ejecutar el proyecto utilizando el siguiente comando:

   ```sh
   # Ejecuta este comando en el CLI.
   python app.py
   ```

   ¡Listo! Ahora deberías poder ejecutar tu proyecto de Python. Si tienes algún problema durante la instalación, revisa cuidadosamente los mensajes de error y asegúrate de seguir los pasos correctamente.

# 🫣 Uso

Puedes ver el funcionamiento de la app 👉🏻[aquí](http://www.isaias.work).

# 👋🏻 Contacto

Si estás interesado en trabajar conmigo o simplemente quieres decir hola, puedes contactarme a través de [isasalas145@gmail.com](mailto:isasalas145@gmail.com), [Whatsapp](https://api.whatsapp.com/send?phone=59170881108&text=%20) o [Twitter](https://twitter.com/isaiahSalah).

Abre la boca

![UwU](https://i.giphy.com/media/3o6Mb6n1senEQtbgdy/giphy.webp)

¡Gracias por tu visita! 🫶🏻🤓
