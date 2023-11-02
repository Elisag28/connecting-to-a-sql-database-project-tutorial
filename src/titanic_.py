import psycopg2
import sqlite3 as sq
import pandas as pd

#Responder a las siguientes preguntas usando SQL sobre la tabla que acabáis de crear:
#1 Cuántos supervivientes hay (columna Survived)
# 2 De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)
# 3. Cuál es el valor del ticket más caro que se compró (columna Fare)

df = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv", sep = ',')


conn = sq.connect('mi_base_de_datos')

cur = conn.cursor()

df.to_sql('mi_base_de_datos', conn, if_exists='replace', index=False)

surv = cur.execute('SELECT COUNT(Survived) FROM mi_base_de_datos WHERE Survived = 1 Group by Survived Order by COUNT(Survived) DESC')

print(f'Total survivors:',{*surv.fetchone()})

sex = cur.execute('SELECT Sex, COUNT(Sex) AS total_passengers FROM mi_base_de_datos Group by Sex Order by Sex')
output = sex.fetchall()

print(f'Total passengers:', {*output})

tick = cur.execute('SELECT MAX(Fare), Fare FROM mi_base_de_datos')

print(f'The most expensive ticket:',{*tick.fetchone()})