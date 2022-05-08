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
  uri = os.getenv('DATABASE_URL')
  if uri and uri.startswith('postgres://'):
    uri = uri.replace('postgres://','postgresql://',1)
  SQLALCHEMY_DATABASE_URI=uri
 

class TestConfig(Config):
  '''
  '''
  pass

class DevConfig(Config):
  '''

  '''
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:whalien52@localhost/pitch'
DEBUG =True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}    