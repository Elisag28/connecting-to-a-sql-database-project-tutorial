import psycopg2
import sqlite3 as sq
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv", sep = ',')


conn = sq.connect('mi_base_de_datos.db')

df.to_sql('mi_base_de_datos.db', conn, if_exists='replace', index=False)

conn.execute("""SELECT * FROM mi_base_de_datos.db""")