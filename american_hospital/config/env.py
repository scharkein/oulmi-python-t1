import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("MYSQL_DATABASE", "american_hospital")
DB_USER = os.getenv("MYSQL_USER", "ah_user")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "")