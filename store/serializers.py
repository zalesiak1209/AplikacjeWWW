from rest_framework import serializers

from .models import Kategoria
from .models import Ogloszenie
from .models import Uzytkownik
from .views import *


class OgloszenieSerializer(serializers.HyperlinkedModelSerializer):
    kategoria = serializers.SlugRelatedField(queryset=Kategoria.objects.all(), slug_field='name')
    wlasciciel = serializers.SlugRelatedField(queryset=Uzytkownik.objects.all(), slug_field='nazwa_uzytkow')

    class Meta:
        model = Ogloszenie
        fields = ['opis', 'kategoria', 'wlasciciel', 'data_dodania', 'marka', 'model', 'rok', 'cena',
                  'numer_telefonu', 'miejscowosc']


class Kategoriaserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class ListaOgloszenSerializer(serializers.HyperlinkedModelSerializer):
    ogloszenie = serializers.SlugRelatedField(queryset=Ogloszenie.objects.all(), slug_field='nazwa_ogloszenia')

    class Meta:
        model = Ogloszenie
        fields = ['nazwa_uzytkow', 'nazwa_ogloszenia', 'numer_telefonu', 'login', 'cena', 'opis']


class Uzytkownikserializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Uzytkownik
        fields = ['nazwa_uzytkow', 'numer_telefonu', 'login', 'email']
