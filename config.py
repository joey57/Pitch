import os
class Config:
  '''
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:whalien52@localhost/pitch'
  SECRET_KEY='123456'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  # simple mde configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
  '''
  '''
  pass

class DevConfig(Config):
  '''

  '''
  DEBUG =True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}    