import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5791628bb0b13ce0c676dfe280ba245'
    
    # Handle both DATABASE_URL and SQLALCHEMY_DATABASE_URI
    database_url = os.environ.get('DATABASE_URL') or os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    
    # Fix postgres:// to postgresql:// for newer SQLAlchemy
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
