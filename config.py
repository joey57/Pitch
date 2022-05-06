import os
class Config:
  '''
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:whalien52@localhost/pitch'
  SECRET_KEY=os.environ.get('12345')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

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