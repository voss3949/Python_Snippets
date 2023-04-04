import pandas as pd
import sqlite3 as sql


df1 = pd.read_csv('C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\Book1.csv')
df2 = pd.read_csv('C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\Book2.csv')

conn = sql.connect('C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\company.db')

df1.to_sql('t1', conn, if_exists='replace', index=False)
df2.to_sql('t2', conn, if_exists='replace', index=False)

result = pd.read_sql_query("SELECT t1.name, t2.department FROM t1 INNER JOIN t2 ON t1.name = t2.name; ", conn)

conn.close()

