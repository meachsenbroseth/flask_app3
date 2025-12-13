import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "sqlite:///" + os.path.join(BASE_DIR, "instance\\users.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = "784500193458-rkenses9hi575474h26vckifvsle0t8g.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "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"

