import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:root@db:3306/flaskdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False