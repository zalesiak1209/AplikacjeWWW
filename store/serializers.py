from rest_framework import serializers

from .models import Kategoria
from .models import Ogloszenie
from .models import Uzytkownik
from .views import *


class Kategoriaserializers(serializers.HyperlinkedModelSerializer):
    name = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Kategorie')

    class Meta:
        model = Kategoria
        fields = ['pk', 'url', 'name']


class OgloszenieSerializer(serializers.HyperlinkedModelSerializer):
    kategoria = serializers.SlugRelatedField(queryset=Kategoria.objects.all(), slug_field='opis')
    nazwa_uzytkow = serializers.ReadOnlyField(source='nazwa_uzytkow.username')

    class Meta:
        model = Ogloszenie
        fields = ['url', 'pk', 'opis', 'kategoria', 'wlasciciel', 'data_dodania', 'marka', 'model', 'rok', 'cena',
                  'numer_telefonu', 'miejscowosc']


class ListaOgloszenSerializer(serializers.HyperlinkedModelSerializer):
    ogloszenie = serializers.SlugRelatedField(queryset=Ogloszenie.objects.all(), slug_field='nazwa_ogloszenia')

    class Meta:
        model = Ogloszenie
        fields = ['pk', 'url', 'nazwa_uzytkow', 'nazwa_ogloszenia', 'numer_telefonu', 'login', 'cena', 'opis']

        def sprawdzenie_ceny(self, ceny):
            if ceny < 0:
                raise serializers.ValidationError("zła cena")
            return ceny


class Uzytkownikserializer(serializers.HyperlinkedModelSerializer):
    ogloszenia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ogloszenie_detal')

    class Meta:
        model = Uzytkownik
        fields = ['url', 'pk', 'nazwa_uzytkownika', 'numer_telefonu', 'login', 'email']
