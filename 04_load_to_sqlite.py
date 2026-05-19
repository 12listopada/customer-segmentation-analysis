import pandas as pd 
import sqlite3 

rfm = pd.read_csv('data/processed/rfm_segmented.csv')
conn = sqlite3.connect('data/processed/customer_segmentation.db')
rfm.to_sql('rfm_segments', conn, if_exists='replace', index=False)

print("Data loaded into SQLite database successfully.")
conn.close()

