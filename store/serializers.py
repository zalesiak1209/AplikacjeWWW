# 3rd-party
from rest_framework import serializers

# Local
from .models import Kategoria
from .models import Ogloszenie
from .models import Uzytkownik


class Kategoriaerializers(serializers.Serializer):
    name = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Kategorie')

    class Meta:
        model = Kategoria
        fields = ['pk', 'url', 'name']


class OgloszenieSerializer(serializers.HyperlinkedModelSerializer):
    kategoria = serializers.SlugRelatedField(queryset=Kategoria.objects.all(), slug_field='opis')
    opis = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='opis')
    wlasciciel = serializers.ReadOnlyField(source='wlasciciel.username')

    class Meta:
        model = Uzytkownik
        fields = ['url', 'pk', 'first_name', 'last_name', 'login', 'numer_telefonu', 'email']


class ListaOgloszenSerializer(serializers.Serializer):
    nazwauzytkownika = serializers.SlugRelatedField(queryset=Uzytkownik.objects.all(), slug_field='login')

    class Meta:
        model = Ogloszenie
        fields = ['pk', 'url', 'opis', 'data_dodania', 'cena', 'model', 'rok']

        def sprawdzenie_ceny(self, ceny):
            if ceny < 0:
                raise serializers.ValidationError("zła cena")
            return ceny
