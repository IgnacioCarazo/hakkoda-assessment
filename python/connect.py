import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv('PASSWORD')
WAREHOUSE = os.getenv('WAREHOUSE')
USER = os.getenv('USER')
ACCOUNT = os.getenv('ACCOUNT')
DATABASE = os.getenv('DATABASE')
SCHEMA = os.getenv('SCHEMA')
ROLE = os.getenv('ROLE')


conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA,
    role=ROLE
)
