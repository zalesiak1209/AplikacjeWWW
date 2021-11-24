from rest_framework import generics

from .models import Kategoria, Ogloszenie
from .serializers import Kategoriaserializers, OgloszenieSerializer
from django_filters import AllValuesFilter, NumberFilter, FilterSet


class kategorialista(generics.ListAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = Kategoriaserializers
    name = 'lista_kategorii'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class Kategoriadetale(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = Kategoriaserializers
    name = 'kategoria_detal'


class Ogloszenielista(generics.ListCreateAPIView):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieSerializer
    name = 'ogloszenie_lista'
    filter_fields = ['marka', 'kategoria', 'data_dodania', 'miejscowosc', 'cena', 'model']
    search_fields = ['marka', 'model']
    ordering_fields = ['marka', 'kategoria', 'model']

    # ?????????????????????permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.uzytkownik)


class Ogloszeniedetal(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieSerializer
    name = 'ogloszenie_detal'


class Ogloszenie_Filter(FilterSet):
    min_cena = NumberFilter(field_name='cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='cena', lookup_expr='lte')
    uzytkownik = AllValuesFilter(field_name='uzytkownik.username')

    class Meta:
        model = Ogloszenie
        fields = ['min_cena', 'max_cena', 'uzytkownik']
