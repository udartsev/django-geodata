import urllib3
import io
from zipfile import ZipFile
import os
from os import listdir
import sys


class GeodataDownloader():

    def __init__(self, code):
        self.code = code
        self.folder = './geodata/data/'
        self.geoname = 'http://download.geonames.org/export/dump/'

    def downloadMainFile(self):
        self.msg('Downloading main file... [%s] ' % self.code)
        http = urllib3.PoolManager()

        # Download and unzip main file
        folder = self.folder + 'main/'
        filename = folder + '%s.zip' % self.code
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(filename):
            response = http.request('GET', self.geoname + '%s.zip' % self.code, preload_content=False)
            with open(filename, 'wb') as f:
                f.write(response.data)

            # Extract contents of zip file
            with ZipFile(filename, 'r') as zipObj:
                zipObj.extractall(folder)

        # self.stdout.write(self.style.SUCCESS('Country %s seeded successfully!' % code))
        self.msg('[OK]', True)

    def downloadAltFile(self):
        self.msg('Downloading alternatenames file... [%s] ' % self.code)
        http = urllib3.PoolManager()

        # Download and unzip main file
        folder = self.folder + 'alt/'
        filename = folder + '%s.zip' % self.code
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(filename):
            response = http.request('GET', self.geoname + 'alternatenames/%s.zip' % self.code, preload_content=False)
            with open(filename, 'wb') as f:
                f.write(response.data)

            # Extract contents of zip file
            with ZipFile(filename, 'r') as zipObj:
                zipObj.extractall(folder)

        # self.stdout.write(self.style.SUCCESS('Country %s seeded successfully!' % code))
        self.msg('[OK]', True)

    def downloadAdmin1Codes(self):
        file = 'admin1CodesASCII.txt'

        self.msg('Downloading %s file... [%s] ' % (file, self.code))
        http = urllib3.PoolManager()

        # Download and unzip main file
        folder = self.folder
        filename = folder + file
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(filename):
            response = http.request('GET', self.geoname + file, preload_content=False)
            with open(filename, 'wb') as f:
                f.write(response.data)

        # self.stdout.write(self.style.SUCCESS('Country %s seeded successfully!' % code))
        self.msg('[OK]', True)

    def downloadAdmin2Codes(self):
        file = 'admin2Codes.txt'

        self.msg('Downloading admin2Codes file... [%s] ' % self.code)
        http = urllib3.PoolManager()

        # Download and unzip main file
        folder = self.folder
        filename = folder + file
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(filename):
            response = http.request('GET', self.geoname + file, preload_content=False)
            with open(filename, 'wb') as f:
                f.write(response.data)

        # self.stdout.write(self.style.SUCCESS('Country %s seeded successfully!' % code))
        self.msg('[OK]', True)

    def downloadTimeZones(self):
        file = 'timeZones.txt'

        self.msg('Downloading timeZones file... [%s] ' % self.code)
        http = urllib3.PoolManager()

        # Download and unzip main file
        folder = self.folder
        filename = folder + file
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(filename):
            response = http.request('GET', self.geoname + file, preload_content=False)
            with open(filename, 'wb') as f:
                f.write(response.data)

        # self.stdout.write(self.style.SUCCESS('Country %s seeded successfully!' % code))
        self.msg('[OK]', True)

    def downloadFeatureCodes(self):
        file = 'featureCodes_%s.txt' % self.code.lower()

        self.msg('Downloading featureCodes file... [%s] ' % self.code)
        http = urllib3.PoolManager()

        # Download and unzip main file
        folder = self.folder
        filename = folder + file
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(filename):
            response = http.request('GET', self.geoname + file, preload_content=False)
            with open(filename, 'wb') as f:
                f.write(response.data)

        # self.stdout.write(self.style.SUCCESS('Country %s seeded successfully!' % code))
        self.msg('[OK]', True)

    def msg(self, msg, n=None):
        sys.stdout.write(msg)
        if n:
            sys.stdout.write("\n")
        sys.stdout.flush()

    def deleteTxt(self, fld=None):
        self.msg('Clear cache... [%s] ' % self.code)
        for file in listdir(self.folder + fld):
            if file.endswith('.txt'):
                os.remove(self.folder + fld + file)
        self.msg('[OK]', True)
