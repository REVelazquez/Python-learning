# from dotenv import load_dotenv
import psycopg2
# import os
import psycopg2.extras

# load_dotenv()

hostname = 'localhost'
database = 'dnd'
username = 'postgres'
pwd= '051994'
port_id= 5432
conn=None

try:
    with psycopg2.connect(
        host = hostname,
        dbname= database,
        user= username,
        password= pwd,
        port=port_id
    ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('DROP TABLE IF EXISTS classes')
            create_script= ''' CREATE TABLE IF NOT EXISTS classes(
            id       int PRIMARY KEY,
            name     varchar(40) NOT NULL,
            url      varchar(100) NOT NULL,
            stats    int
            )'''

            cur.execute(create_script)

            insert_script = 'INSERT INTO classes (id, name, url, stats) VALUES( %s, %s, %s, %s)'
            insert_values=[(1, 'Barbarian', 'https://www.dnd5eapi.co/api/classes/barbarian', 10), (2, 'Bard', 'https://www.dnd5eapi.co/api/bard/bard', 15)]
            for record in insert_values:
                cur.execute(insert_script, record)

            cur.execute('SELECT * FROM CLASSES')
            for record in cur.fetchall():
                print(record['name'], record['stats'])


            update_script = 'UPDATE dnd SET stats= stats+(stats*0.5) '

            delete_script = 'DELETE FROM classes WHERE name = %s'
            delete_record = ('Bard',)
            cur.execute(delete_script, delete_record)
        conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()
        