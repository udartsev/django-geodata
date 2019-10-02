import sys
import time
import psycopg2


class GeodataAltSeeder():

    def __init__(self, code, db):
        self.code = code
        self.folder = 'geodata/data/'
        self.file = self.folder + 'alt/%s.txt' % code.upper()
        # Connect to DB
        self.conn = psycopg2.connect(
            dbname=db['name'],
            user=db['user'],
            password=db['password'],
            host=db['host']
        )

    def seed(self):
        # Read data from file
        print("\nRead file: " + str(self.file))
        data_list = self.getDataFromFile(self.file)
        total_len = len(data_list)
        count = 0
        print("Total: " + str(total_len) + "\n")

        # Create table in the database
        tableName = "%s_alternate" % self.code.lower()
        print("Create table... [%s]" % tableName)
        self.createAlternateTable(self.conn, tableName)

        # Insert data into table
        sys.stdout.write("""Insert into database...""")

        for line in data_list:
            self.insertIntoAltNames(self.conn, line)
            count = count + 1
            if count % 100 == 0:
                sys.stdout.write(""".""")
                sys.stdout.flush()
            if count % 10000 == 0:
                message = """[%s] from [%s] DONE""" % (count, total_len)
                sys.stdout.write(message)
                sys.stdout.flush()

        self.conn.close()

        # Print done message
        print("/################# MAIN DONE ##################/")

    #############################
    # Create alternate table
    #############################
    def createAlternateTable(self, conn, tableName):
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
    def getDataFromFile(self, file):
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
    def insertIntoAltNames(self, conn, row):
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
