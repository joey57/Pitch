import os
class Config:
  '''
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:whalien52@localhost/pitch'
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  # simple mde configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
  '''
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
  '''
  '''
  pass

class DevConfig(Config):
  '''

  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:whalien52@localhost/pitch'
DEBUG =True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}    