import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
env_path = Path(".") / '.env'
load_dotenv(dotenv_path=env_path)

DATABASE_NAME = os.getenv("DATABASE_NAME", "bar")
DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
DATABASE_URL = os.getenv("DATABASE_URL",
                         f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@"
                         f"{DATABASE_HOST}:{DATABASE_PORT}/bar")
DEBUG = os.getenv("DEBUG", False)
