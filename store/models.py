from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=255, null=False, unique=True, verbose_name='Kategoria')

    class Meta:
        ordering = ['nazwa']

    def __str__(self):
        return self.nazwa


class Uzytkownik(AbstractUser):
    pass


class Ogloszenie(models.Model):
    opis = models.CharField(max_length=255, null=True, unique=False)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    wlasciciel = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add=True)
    marka = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=50, null=False)
    rok = models.DecimalField(max_digits=4, decimal_places=0, null=False)
    cena = models.DecimalField(decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.01'))],
                               null=False)
    numer_telefonu = models.DecimalField(decimal_places=0, max_digits=9, null=False, unique=True)
    miejscowosc = models.CharField(max_length=255, null=True)
