from django.core.management.base import BaseCommand, CommandError
import os
from os import listdir
import sys
from geodata.geodataDownloader import GeodataDownloader
from geodata.geodataMainSeeder import GeodataMainSeeder
from geodata.geodataAltSeeder import GeodataAltSeeder


class Command(BaseCommand):
    help = 'geodata seeder'

    def add_arguments(self, parser):
        parser.add_argument(
            'countryCode',
            type=str,
            help='Country code. Example: RU, US, GB, FR, DE...')

        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete seeded tables from `geodata` database',
        )

        # Named (optional) arguments
        parser.add_argument(
            '--mysql',
            action='store_true',
            help='Seed into MySQL database',
        )

    def handle(self, *args, **options):
        #############################
        # 1. WELCOME MESSAGE
        #############################
        # Print welcome message_from_bytes(s, _class=email.message.Message, *, policy=policy.compat32)
        print("/########################################################################/")
        print("/########################  GEODATA FOR DJANGO  ##########################/")
        print("/########################################################################/")

        #############################
        # 2. GETTING VARS
        #############################
        self.code = str(options['countryCode']).upper()
        # self.conn =

        if self.code is None:
            raise CommandError('Country "%s" does not exist' % self.code)

        #############################
        # 3. DOWNLOAD RAW FILES
        #############################
        d = GeodataDownloader(self.code)
        d.downloadMainFile()
        d.downloadAltFile()
        d.downloadAdmin1Codes()
        d.downloadAdmin2Codes()
        d.downloadTimeZones()
        d.downloadFeatureCodes()

        #############################
        # 4. SET DATABASE SETTINGS
        #############################
        db = {}
        db['name'] = 'geodata'
        db['user'] = 'postgres'
        db['password'] = 'Postgres911!'
        db['host'] = 'localhost'

        #############################
        # 5. SEED DATA TO DATABASE
        #############################
        #GeodataMainSeeder(self.code, db).seed()  #OK
        GeodataAltSeeder(self.code, db).seed()

        #############################
        # __. DELETE RAW FILES
        #############################
        # self.deleteTxt('./main/')
        # self.deleteTxt('./alt/')

    def msg(self, msg, n=None):
        sys.stdout.write(msg)
        if n:
            sys.stdout.write("\n")
        sys.stdout.flush()
