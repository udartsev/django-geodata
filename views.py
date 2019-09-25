from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from intravel.utils import get_body_in_request
from rest_framework.views import APIView
from geodata.repositories import GeodataRepository
from django.core.serializers import serialize
from geodata.serializers import GeodataModelRuSerializer, GeodataCitiesSerializer, GeodataCitiesSerializer2, GeodataCitiesSerializer3
from djangorestframework_camel_case.util import camelize
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from intravel_auth.permissions import IsAdminGroup
from intravel_auth.repositories import FirebaseAuthRepository, AuthRepository, UsersRepository, FacebookAuthRepository, \
    VkAuthRepository, GmailAuthRepository, ProfilesRepository
from intravel_auth.serializers import ProfilesSerializer, PostProfilesSerializer, UsersProfileSerializer, \
    PrivateSettingsSerializer, UsersProfileLiteSerializer

import json
from SimpleDump import dd, dump

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from intravel.errors.exceptions import EntityDoesNotExistException
from intravel.errors.http_exception import HttpException
from intravel.errors.errors import Errors
from intravel.mappers import RequestToPaginationMapper

from geodata import exceptions


class FirstCity(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data = GeodataRepository.getFirstOneCityName()
        results = GeodataModelRuSerializer(data, many=True)
        return Response(camelize(results.data), status=200)


class AllCities(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        countrycode = kwargs.get('code', None)
        data = GeodataRepository.getAllCitiesByCountryCode(countrycode)
        # results = GeodataCitiesSerializer(data, many=True)
        results = GeodataCitiesSerializer2(data, many=True)
        return Response(camelize(results.data), status=200)

    def post(self, request, *args, **kwargs):
        countrycode = kwargs.get('code', None)
        search = request.data.get('search', None)

        if search is None:
            raise exceptions.SearchFieldRequiered()

        pagination = RequestToPaginationMapper.map(request)
        data = GeodataRepository.searchCities(countrycode, search, pagination)
        results = GeodataCitiesSerializer2(data, many=True)
        return Response(camelize(results.data), status=200)


class AllCitiesSearch(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        search = request.data.get('search')

        countrycode = kwargs.get('code', None)

        """snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)"""

        data = GeodataRepository.searchCities(countrycode, str(search))
        # results = GeodataCitiesSerializer(data, many=True)
        results = GeodataCitiesSerializer2(data, many=True)
        return Response(camelize(results.data), status=200)
