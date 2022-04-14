import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a lmn-bot').read()[:-1]
#DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

create_table_query = '''CREATE TABLE training(
   record_no serial PRIMARY KEY,
   training_name VARCHAR (50) NOT NULL,
   training VARCHAR (50) NOT NULL,
   duration INTERVAL NOT NULL,
   date DATE NOT NULL
);'''



delete_table_query = '''DROP TABLE IF EXISTS training'''



print("Done")

cursor.execute(create_table_query)
conn.commit()

cursor.close()
conn.close()