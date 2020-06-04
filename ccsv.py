import psycopg2
import csv

con = psycopg2.connect(database="pickuppoint", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()
cur.execute("SELECT * FROM public.acms_partner")
rows = cur.fetchall()

with open('acmss.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(rows)


print("Operation done successfully")
con.close()