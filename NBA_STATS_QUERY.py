import pandas as pd
import sqlite3 as sql

df = pd.read_csv('C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\nba_example.tsv', sep='\t')

# df.to_html('C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\nba_to_html.html')

# Connect to the database
conn = sql.connect('C:\\Users\\12245\\OneDrive\\Documents\\Python_Projects\\Data\\nba_stats_example.db')

# Write the DataFrame to the database as a table
table_name = 'nba_stats'

df.to_sql(table_name, conn, if_exists='replace')

query = 'SELECT * FROM nba_stats WHERE AST > 6'

df_query = pd.read_sql_query(query, conn)

print(df_query)
print(df_query['AST'].describe())

# Close the connection
conn.close()

