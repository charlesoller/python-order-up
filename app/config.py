"""Flask app configuration"""

import os

class Configuration:
    """Configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    