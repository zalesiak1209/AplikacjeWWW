from django.http import QueryDict
from rest_framework import generics, permissions, viewsets, serializers

from .custompermission import IsCurrentUserOwnerOrReadOnly
from .models import Ogloszenie, Kategoria, Uzytkownik
from .serializers import Kategoriaserializers, OgloszenieSerializer, Uzytkownikserializer
from django_filters import AllValuesFilter, NumberFilter, FilterSet


class kategorialista(viewsets.ModelViewSet):
    queryset = Kategoria.objects.filter()
    serializer_class = Kategoriaserializers
    name = 'kategorialista'
    filterset_fields = ['name']
    search_fields = ['name', 'queryset']
    ordering_fields = ['name']

    def getNumbers(self):
        return 'one','two'
    one,two=getNumbers()

    # def __getitem__(self, item):
    #     return self.Kategoria


class Uzytkowniklista(viewsets.ModelViewSet):
    queryset = Uzytkownik.objects.all()
    serializer_class = Uzytkownikserializer
    name = 'uzytkowniklista'
    filterset_fields = ['nazwa_uzytkow']
    search_fields = ['nazwa_uzytkow']
    ordering_fields = ['nazwa_uzytkow']


class Ogloszenielista(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieSerializer
    name = 'ogloszenielista'
    filter_fields = ['marka', 'kategoria', 'data_dodania', 'miejscowosc', 'cena', 'model']
    search_fields = ['marka', 'model']
    ordering_fields = ['marka', 'kategoria', 'model']

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.uzytkownik)


class Ogloszenie_Filter(FilterSet):
    min_cena = NumberFilter(field_name='cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='cena', lookup_expr='lte')
    uzytkownik = AllValuesFilter(field_name='uzytkownik.username')

    class Meta:
        model = Ogloszenie
        fields = ['min_cena', 'max_cena', 'uzytkownik']
