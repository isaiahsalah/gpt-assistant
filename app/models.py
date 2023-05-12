"""
Este módulo dispone de la conexión a la base de datos de Mongo 
y las diferentes operaciones realacionada con la lectura y escritura de datos
"""
from app import app, chatgpt
from flask_pymongo import PyMongo

mongo = PyMongo(app)


def add_chat(message, from_number):
    """
    Esta función agrega un nuevo mensaje a la conversación de un usuario y devuelve la respuesta de ChatGPT.

    Args:
        message (str): El mensaje enviado por el usuario.
        from_number (str): El número de teléfono del usuario.

    Returns:
        str: La respuesta de ChatGPT.
    """
    # Consulta la existencia del usuario en la DB con su número de Whatsapp
    conversation = mongo.db.chat.find_one({'phone': from_number})
    # Si el usuario ya existe en la DB, se actualiza la conversación con el nuevo mensaje.
    if conversation:
        # Si el número de mensajes en la conversación es mayor o igual a 50, se redirige al usuario a un contacto.
        if len(conversation['messages']) >= 22:
            return '/contact'
        conversation['messages'].append({"role": "user", "content": message})
    # Si el usuario no existe en la DB, se crea una nueva conversación con el mensaje del usuario.
    else:
        conversation = {
            'phone': from_number,
            'messages': [chatgpt.context, {"role": "user", "content": message}]
        }
    # Se envía el contexto de la conversación a la API de Chatgpt y se guarda la respuesta en una variable.
    gpt_response = chatgpt.gpt_response(msg_context=conversation['messages'])
    # Se añade la respuesta de ChatGPT al contexto de la conversación.
    conversation['messages'].append(gpt_response)
    # Se actualiza la conversación en la DB.
    mongo.db.chat.update_one(
        {'phone': from_number},
        {"$set": {'messages': conversation['messages']}}, upsert=True)

    # Se devuelve la respuesta de ChatGPT.
    return gpt_response.content
