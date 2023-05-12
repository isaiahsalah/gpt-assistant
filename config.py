"""
Este módulo contiene la configuración de la aplicación. Define las variables 
de entorno necesarias para la ejecución de la aplicación en diferentes 
entornos (desarrollo, producción, etc.), incluyendo las claves de API, 
tokens de autenticación y URL de base de datos MongoDB. Además, define 
dos subclases de configuración: DevelopmentConfig y ProductionConfig, 
cada una con diferentes configuraciones específicas para su entorno 
correspondiente.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """
    Esta clase define la configuración de la aplicación. 
    Define valores por defecto para las variables de 
    entorno necesarias para que la aplicación funcione correctamente.
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    API_KEY_GPT = os.environ.get('API_KEY_OPENAI') or 'No existe'
    API_KEY_WHATS = os.environ.get('API_KEY_WHATS') or 'No existe'
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN') or 'No existe'
    MONGO_URI = os.environ.get('MONGO_URI') or 'No existe'

    CONTEXT_GTP = os.environ.get('CONTEXT_GTP') or 'No existe'


class DevelopmentConfig(Config):
    """
    Clase que hereda de Config y define configuraciones específicas para el entorno de desarrollo.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Clase que hereda de Config y define configuraciones específicas para el entorno de producción.
    """
    DEBUG = False
