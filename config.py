from dotenv import load_dotenv
import os

load_dotenv()
jwt_secret = os.getenv("JWT_SECRET")
