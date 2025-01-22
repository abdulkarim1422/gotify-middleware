import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Access environment variables

# Gotify
GOTIFY_URL = os.getenv('GOTIFY_URL')
GOTIFY_ADMIN_TOKEN = os.getenv('GOTIFY_ADMIN_TOKEN') # must be stable token

# DB
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
