from rest_framework import serializers
from geodata.models import GeodataModelRu, GeodataModelRuAlternate


class GeodataModelRuSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeodataModelRu
        fields = (
            '__all__'
        )


class GeodataCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeodataModelRu
        fields = (
            "geonameid", "name", "latitude", "longitude", "admin1code"
        )


class GeodataCitiesSerializer2(serializers.ModelSerializer):
    geonameid = GeodataCitiesSerializer()

    class Meta:
        model = GeodataModelRuAlternate
        fields = (
            "geonameid", "alternate_name", "isolanguage"
        )


class GeodataCitiesSerializer3(serializers.ModelSerializer):
    class Meta:
        model = GeodataModelRu
        fields = (
            "__all__"
        )
