import os
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the psycopg2 function
import psycopg2

con = psycopg2.connect(host = "localhost",
    user = "gitpod", 
    password = "postgres",
    database = "my_db",
)

cur = con.cursor()
# 2) Execute the SQL sentences to create your tables using the psycopg2 execute function
# It's done

# 3) Execute the SQL sentences to insert your data using the psycopg2 execute function 
#It's done

# 4) Use pandas to print one of the tables as dataframes using read_sql function
tabla = pd.read_sql('SELECT * FROM book_authors;', con) 
print(tabla) 