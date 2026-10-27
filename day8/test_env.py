import os
from dotenv import load_dotenv

load_dotenv()

print("user:", os.environ.get("DB_USER"))
print("dsn:", os.environ.get("DB_DSN"))
print("password length:", len(os.environ.get("DB_PASSWORD", "")))