# django-geodata
Django app to add GEO data [Countries, Cities, Time Zones, Geo Points and their Polygons in geoJSON format.]

## Install
1) Download Django app packege:
`pip require django-geodata`

***
2) Seed geo data for example Russia (contry code = RU) data or use US, GB, FR, DE or other valid country code
`python manage.py seetcountry RU` 

***
3) Add to your django `settings.py` file database connection settings for **geodata** table: 

        DATABASE_ROUTERS = ['geodata.databaserouter.GeodataRouter']
        DATABASE_APPS_MAPPING = {'geodata': 'geodata'}
        DATABASES = {
            'geodata': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'geodata',
            'USER': 'postgres',
            'PASSWORD': 'Postgres911!',
            'HOST': 'localhost',
            'PORT': '5432'
        }
***
4)  Add to your django `urls.py`:

        urlpatterns = [
            path('api/', include('geodata.urls')),
        ]

***
5) `python manage.py runserver`
