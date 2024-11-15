import os
from dotenv import load_dotenv

# 加載 .env 文件中的環境變量
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    PORT = int(os.getenv('PORT', 5000))


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
