import os

from dotenv import load_dotenv

# loading dotenv to load .env files
load_dotenv()

# processing .env files
DATABASE_URL = os.getenv("DATABASE_URL")
PORT = os.getenv("PORT")
