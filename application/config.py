import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
SA_CLIENT_ID = os.getenv("SA_CLIENT_ID")