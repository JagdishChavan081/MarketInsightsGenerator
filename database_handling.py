import psycopg2

hostname = "localhost"
database = "Finance"
username = "postgres"
pwd = "1234"
port_id = 5432
conn = None
curr = None


try:
    conn = psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    )

    cur = conn.cursor()

    create_script = """CREATE TABLE iF NOT EXISTS stock(
                    date_time TIMESTAMP PRIMARY KEY,
                    open_price FLOAT,
                    high_price FLOAT,
                    low_price FLOAT,
                    close_price FLOAT)"""

    cur.execute(create_script)

    cur.execute("SELECT * FROM stock")
    print(cur.fetchall())
    conn.commit()


except Exception as error:
    print(error)

finally:
    if curr is not None:
        cur.close()
    if conn is not None:
        conn.close()
