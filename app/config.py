import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost/my_project_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")
    PAGINATION_DEFAULT_SIZE = 10
    PAGINATION_MAX_SIZE = 50
    DEBUG = True
