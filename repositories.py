import json
import os

import requests
from channels.db import database_sync_to_async
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from oauth2_provider.models import Application, AccessToken
from rest_framework.authtoken.models import Token
from django.contrib.gis.geos import GEOSGeometry
from intravel.network import Pagination

from geodata.models import GeodataModelRu, GeodataModelRuAlternate


class GeodataRepository:

    def getFirstOneCity():
        data = GeodataModelRu.objects.all()
        return data[:1]

    def getFirstOneCityName():
        data = GeodataModelRu.objects.all()
        return data[:1]

    def searchCities(code, search, pagination=None):
        # alternate_name__icontains - for `like` search
        # alternate_name__startswith
        if search is None:
            data = GeodataModelRuAlternate.objects.filter(isolanguage=str(code).lower())[
                pagination.offset:pagination.limit]
        else:
            data = GeodataModelRuAlternate.objects.filter(isolanguage=str(
                code).lower(), alternate_name__startswith=str(search))[pagination.offset:pagination.limit]
        return data
