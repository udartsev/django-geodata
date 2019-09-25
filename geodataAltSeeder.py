import sys
import time
import psycopg2
import os

from SimpleDump import dd
#############################
# PostgreSQL SETTINGS
#############################
# Connect to DB

conn = psycopg2.connect(dbname='geodata', user='postgres', password='Postgres911!', host='localhost')
file = './ALTNAMES/RU.txt'


#############################
# Create country table
#############################
def createAlternateTable(conn, tableName):
    query = '''
    CREATE TABLE IF NOT EXISTS %s (
    alternateNameId int PRIMARY KEY,
    geonameid int REFERENCES ru(geonameid),
    isolanguage varchar(20) NULL,
    alternate_name varchar(400) NULL,
    isPreferredName boolean NULL,
    isShortName boolean NULL,
    isColloquial boolean NULL,
    isHistoric boolean NULL,
    from_date varchar(40) NULL,
    to_date varchar(40) NULL)
    ''' % (tableName)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return
#############################
# Get data from file
#############################


def getDataFromFile(file):
    data_file = open(file, 'r')
    data_list = []
    for line in data_file:
        if line.endswith("\n"):
            line = line[:-1]
        if line.endswith("\r\n"):
            line = line[:-2]
        row = line.split("\t")
        for i, val in enumerate(row):
            if "".__eq__(val):
                row[i] = None
        data_list.append(row)
    return data_list
#############################
# Insert Data into Table
#############################


def insertIntoAltNames(conn, row):
    query = """
    INSERT INTO ru_alternate
    (alternateNameId,
    geonameid,
    isolanguage,
    alternate_name,
    isPreferredName,
    isShortName,
    isColloquial,
    isHistoric,
    from_date,
    to_date
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT DO NOTHING
    """
    cursor = conn.cursor()
    cursor.execute(query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    conn.commit()
    cursor.close()


# Print welcome message
print("/########################################################################/")
print("/##############################  GEODATA ################################/")
print("/########################### GEONAMES SEEDER ############################/")
print("/############################## POSTGRESQL ##############################/")
print("/########################################################################/")

# Read data from file
print("Читаем данные из файла: " + str(file))
data_list = getDataFromFile(file)
total_len = len(data_list)
count = 0
print("Всего записей: " + str(total_len) + "\n")

# Create table in the database
print("Создаем таблицу...")
createAlternateTable(conn, """ru_alternate""")

# Insert data into table
sys.stdout.write("""Записываем в БД...""")

for line in data_list:
    insertIntoAltNames(conn, line)
    count = count + 1
    if count % 100 == 0:
        sys.stdout.write(""".""")
        sys.stdout.flush()
    if count % 10000 == 0:
        message = """[%s] из [%s] DONE""" % (count, total_len)
        sys.stdout.write(message)
        sys.stdout.flush()

conn.close()

# Print done message
print("/#####################################################################/")
print("/##############################  EXIT ################################/")
print("/#####################################################################/")
