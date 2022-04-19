import psycopg2
import os

def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(training_name, training, duration, date)'
    postgres_insert_query = f"""INSERT INTO training {table_columns} VALUES (%s,%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 training 表單！"
    print(message)

    cursor.close()
    conn.close()
    
    return message

def web_select_overall():
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_select_query = f"""SELECT * FROM training ORDER BY record_no;"""
    
    cursor.execute(postgres_select_query)
    
    message = []
    while True:
        temp = cursor.fetchmany(10)
        
        if temp:
            message.extend(temp)
        else:
            break
    
    cursor.close()
    conn.close()
    
    return message


def web_select_specific(condition):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    condition_query = []
    
    for key, value in condition.items():
        if value:
            condition_query.append(f"{key}={value}")
    if condition_query:
        condition_query = "WHERE " + ' AND '.join(condition_query)
    else:
        condition_query = ''
    
    postgres_select_query = f"""SELECT * FROM training {condition_query} ORDER BY record_no;"""
    print(postgres_select_query)
    
    cursor.execute(postgres_select_query)

    table = []
    while True:
        temp = cursor.fetchmany(10)

        if temp:
            table.extend(temp)
        else:
            break

    cursor.close()
    conn.close()

    return table 