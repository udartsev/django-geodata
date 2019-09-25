import sys
import time
import psycopg2


class GeodataMainSeeder():

    def __init__(self, code, db):
        self.code = code
        self.folder = 'geodata/data/'
        self.file = self.folder + 'main/%s.txt' % code.upper()
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
        print("Create table... [%s]" % self.code.lower())
        self.createCountryTable(self.conn, self.code.lower())

        # Insert data into table
        sys.stdout.write("""Insert into database...""")

        for line in data_list:
            self.insertIntoCountry(self.conn, line)
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
    # Create country table
    #############################
    def createCountryTable(self, conn, tableName):
        query = '''
        CREATE TABLE IF NOT EXISTS %s (
        geonameid int PRIMARY KEY,
        name varchar(200) NULL,
        asciiname varchar(200) NULL,
        alternatenames varchar(10000) NULL,
        latitude float8 NULL,
        longitude float8 NULL,
        featureclass char(1) NULL,
        featurecode varchar(10) NULL,
        countrycode varchar(10) NULL,
        cc2 varchar(200) NULL,
        admin1code varchar(20) NULL,
        admin2code varchar(80) NULL,
        admin3code varchar(20) NULL,
        admin4code varchar(20) NULL,
        population bigint NULL,
        elevation int NULL,
        dem text NULL,
        timezone varchar(40) NULL,
        modificationdate varchar(40) NULL)
        ''' % (tableName)

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()

        return

    #############################
    # Get data from file
    #############################
    def getDataFromFile(self, file=None):
        if file is None:
            file = self.file

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
    def insertIntoCountry(self, conn, row):
        query = """
        INSERT INTO ru
        (geonameid,
        name,
        asciiname,
        alternatenames,
        latitude,
        longitude,
        featureclass,
        featurecode,
        countrycode,
        cc2,
        admin1code,
        admin2code,
        admin3code,
        admin4code,
        population,
        elevation,
        dem,
        timezone,
        modificationdate)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT DO NOTHING
        """

        cursor = conn.cursor()
        cursor.execute(query, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                               row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))
        conn.commit()
        cursor.close()
