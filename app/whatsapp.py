"""
Este módulo es una colección de funciones que permiten interactuar con 
la API de WhatsApp Business de Facebook. En particular, se puede enviar 
mensajes de texto y de contacto a un número de WhatsApp específico, y 
verificar la autenticidad de una solicitud de webhook. Además, las funciones 
utilizan la biblioteca requests de Python para enviar solicitudes HTTP 
a la API de WhatsApp.
"""
import json
import requests
from app import app


token_whats = app.config['API_KEY_WHATS']
verify_token = app.config['VERIFY_TOKEN']


def send_text_message(phone_number_id, from_number, message_content):
    """
    Función para enviar un mensaje de texto a un número de teléfono.

    Args: 
        phone_number_id: ID del número de teléfono en Facebook.
        from_number: Número de teléfono del usuario.
        message_content: Contenido del mensaje.
    """
    payload = json.dumps({
        'messaging_product': 'whatsapp',
        "recipient_type": "individual",
        'to': from_number,
        "type": "text",
        'text': {
            "preview_url": False,
            'body': message_content}
    })

    headers = {
        'Content-Type': 'application/json'
    }

    # Realizar la petición HTTP POST al API de Facebook para enviar el mensaje.
    requests.post(
        f'https://graph.facebook.com/v16.0/{phone_number_id}/messages?access_token={token_whats}',
        headers=headers,
        data=payload,
        timeout=10
    )


def send_contact_message(phone_number_id, from_number):
    """
    Función para enviar un mensaje de contacto a un número de teléfono.

    Args:  
        phone_number_id: ID del número de teléfono en Facebook.
        from_number: Número de teléfono del usuario.
    """
    payload = json.dumps({
        'messaging_product': 'whatsapp',
        "recipient_type": "individual",
        'to': from_number,
        "type": "contacts",
        "contacts": [{
            "emails": [{
                "email": "Isasalas145@gmail.com"
            }],
            "name": {
                "formatted_name": "Isaiah",
                "first_name": "Isaiah",
                "last_name": "Salah",
                "suffix": "(dev)"
            },
            "org": {
                "department": "Santa Cruz Bolivia",
                "title": "Desarrollador"
            },
            "phones": [{
                "phone": "+59170881108",
                "wa_id": "59170881108"
            }],
            "urls": [{
                "url": "isaias.lat"
            }]
        }]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    # Realizar la petición HTTP POST al API de Facebook para enviar el mensaje de contacto.
    requests.post(
        f'https://graph.facebook.com/v16.0/{phone_number_id}/messages?access_token={token_whats}',
        headers=headers,
        data=payload,
        timeout=10
    )


def verify_webhook(mode, token, challenge):
    """
    Función para verificar el webhook de Facebook.

    Args: 
        mode: Modo del webhook.
        token: Token de verificación.
        challenge: Desafío de verificación.
    """
    if mode and token:
        if mode == 'subscribe' and token == verify_token:
            print('WEBHOOK_VERIFIED')
            return challenge, 200
        else:
            return 'Verification token mismatch', 403
    else:
        return 'Bad request', 400
