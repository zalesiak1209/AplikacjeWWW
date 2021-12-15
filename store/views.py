from rest_framework import permissions, viewsets

from .custompermission import IsCurrentUserOwnerOrReadOnly
from .models import Ogloszenie, Kategoria, Uzytkownik
from .serializers import Kategoriaserializers, OgloszenieSerializer, Uzytkownikserializer
from django_filters import AllValuesFilter, NumberFilter, FilterSet


class Ogloszenie_Filter(FilterSet):
    min_cena = NumberFilter(field_name='cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='cena', lookup_expr='lte')

    class Meta:
        model = Ogloszenie
        fields = ['min_cena', 'max_cena']


class kategorialista(viewsets.ModelViewSet):
    queryset = Kategoria.objects.filter()
    serializer_class = Kategoriaserializers
    name = 'kategorialista'
    filterset_fields = ['name']
    search_fields = ['name', 'queryset']
    ordering_fields = ['name']

    # def getNumbers(self):
    #     return 'one','two'
    # one,two=getNumbers()

    # def __getitem__(self, item):
    #     return self.Kategoria


class Uzytkowniklista(viewsets.ReadOnlyModelViewSet):
    queryset = Uzytkownik.objects.all()
    serializer_class = Uzytkownikserializer
    name = 'uzytkowniklista'
    search_fields = ['username']
    permission_classes = [permissions.IsAdminUser]


class Ogloszenielista(viewsets.ModelViewSet):
    queryset = Ogloszenie.objects.all()
    serializer_class = OgloszenieSerializer
    filter_class = Ogloszenie_Filter
    name = 'ogloszenielista'
    filter_fields = ['marka', 'kategoria', 'data_dodania', 'miejscowosc', 'cena', 'model']
    search_fields = ['marka', 'model']
    ordering_fields = ['marka', 'kategoria', 'model']

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(wlasciciel=self.request.user)
