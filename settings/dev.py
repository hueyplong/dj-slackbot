from .base import *
import environ


# Read the .env file for environment variables
base = environ.Path(__file__) - 2
env = environ.Env()
environ.Env.read_env(env_file=base(".env"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {"default": env.db("DATABASE_URL")}
