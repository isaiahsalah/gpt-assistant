"""
Este módulo contiene dos rutas de Flask que manejan la API de WhatsApp. La ruta "/webhook" 
maneja la recepción de mensajes y la respuesta de ChatGPT a través de la API de WhatsApp. 
La ruta "/webhook" también maneja el proceso de verificación del webhook. El módulo utiliza 
funciones de los módulos app, models y whatsapp para enviar y recibir mensajes a través 
de la API de WhatsApp.
"""

from app import app, models, whatsapp
from flask import request


@app.route('/webhook', methods=['POST'])
def webhook():
    """Esta función maneja el webhook para recibir y enviar mensajes a través de la API de WhatsApp."""

    # Obtiene el cuerpo de la solicitud POST como un objeto JSON
    body = request.get_json()

    # Verifica que el objeto JSON tenga una clave 'object'
    if body['object']:
        # Verifica que el objeto JSON tenga ciertas claves y valores necesarios
        if body['entry'] and body['entry'][0]['changes'] and body['entry'][0]['changes'][0] and body['entry'][0]['changes'][0]['value']['messages'] and body['entry'][0]['changes'][0]['value']['messages'][0]:

            # Obtiene el número de teléfono del usuario y el mensaje enviado por el usuario
            phone_number_id = body['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
            from_number = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
            msg_body = body['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

            # Agrega el mensaje del usuario a la conversación y obtiene la respuesta de ChatGPT
            response = models.add_chat(
                message=msg_body, from_number=from_number)

            # Si la respuesta es "/contact", envía un mensaje de contacto al usuario
            if response == "/contact":
                whatsapp.send_text_message(
                from_number=from_number,
                phone_number_id=phone_number_id,
                message_content='Excediste los 10 mensajes🫣, si quieres saber más de como se hizo esto, puedes hablar conmigo👇🏻')
                whatsapp.send_contact_message(
                    from_number=from_number,
                    phone_number_id=phone_number_id)
                return 'Success', 200

            # Envía la respuesta de ChatGPT al usuario
            whatsapp.send_text_message(
                from_number=from_number,
                phone_number_id=phone_number_id,
                message_content=response)
            return 'Success', 200
        else:
            # Si el objeto JSON no tiene los valores esperados, devuelve una respuesta de error
            return 'Success', 200
    else:
        # Si el objeto JSON no tiene la clave 'object', devuelve una respuesta de error
        return 'Not Found', 404


@app.route('/webhook')
def verify():
    """Esta función maneja el proceso de verificación del webhook."""

    # Obtiene los parámetros de la solicitud GET
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    # Verifica el token y devuelve el valor del desafío si es correcto
    response = whatsapp.verify_webhook(
        challenge=challenge, mode=mode, token=token)

    # Devuelve la respuesta de verificación
    return response
