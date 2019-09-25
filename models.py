# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models
# import tsvector_field


class GeodataModelRu(models.Model):
    geonameid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    asciiname = models.CharField(max_length=200, blank=True, null=True)
    alternatenames = models.CharField(max_length=10000, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    featureclass = models.CharField(max_length=1, blank=True, null=True)
    featurecode = models.CharField(max_length=10, blank=True, null=True)
    countrycode = models.CharField(max_length=10, blank=True, null=True)
    cc2 = models.CharField(max_length=200, blank=True, null=True)
    admin1code = models.CharField(max_length=20, blank=True, null=True)
    admin2code = models.CharField(max_length=80, blank=True, null=True)
    admin3code = models.CharField(max_length=20, blank=True, null=True)
    admin4code = models.CharField(max_length=20, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    dem = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=40, blank=True, null=True)
    modificationdate = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ru'


class GeodataModelRuAlternate(models.Model):
    alternatenameid = models.IntegerField(primary_key=True)
    geonameid = models.ForeignKey(GeodataModelRu, models.DO_NOTHING, db_column='geonameid', blank=True, null=True)
    isolanguage = models.CharField(max_length=20, blank=True, null=True)
    alternate_name = models.CharField(max_length=400, blank=True, null=True)
    ispreferredname = models.BooleanField(blank=True, null=True)
    isshortname = models.BooleanField(blank=True, null=True)
    iscolloquial = models.BooleanField(blank=True, null=True)
    ishistoric = models.BooleanField(blank=True, null=True)
    from_date = models.CharField(max_length=40, blank=True, null=True)
    to_date = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ru_alternate'
