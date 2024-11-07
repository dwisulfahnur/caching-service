import os
import sys
from dotenv import load_dotenv

load_dotenv()

TESTING = "pytest" in sys.modules or os.getenv("TESTING", "False") == "True"

if TESTING:
    DATABASE_URL = "sqlite:///./test_database.db"
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cache.db")
