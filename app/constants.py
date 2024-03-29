import os
from dotenv import load_dotenv

load_dotenv()

PWD_HASH_SALT = str.encode(os.environ.get("PWD_HASH_SALT"))
PWD_HASH_ITERATIONS = int(os.environ.get("PWD_HASH_ITERATIONS"))
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
