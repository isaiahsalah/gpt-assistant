"""
Este módulo inicia la aplicación Flask de la aplicación cuando se 
ejecuta como un programa independiente. 
"""
from app import app

if __name__ == '__main__':
    # Ejecuta la aplicación Flask para recibir solicitudes HTTP
    app.run()
