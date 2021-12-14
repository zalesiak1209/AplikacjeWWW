# Django
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Kategoria(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, verbose_name='Kategoria')

    class Meta:
        ordering = ['name']

        def __str__(self):
            return self.name


class Uzytkownik(models.Model):
    nazwa_uzytkow = models.CharField(max_length=20, null=False, unique=True)
    numer_telefonu = models.CharField(max_length=9, null=False, unique=True)
    login = models.CharField(max_length=9, null=False, unique=True)
    haslo = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=32, null=False, unique=True)

    def create_user(self, email, haslo=None):
        if not email:
            raise ValueError('Musisz podać adres email.')

        uzytkownik = self.model(
            email=self.normalize_email(email),
        )

        uzytkownik.set_password(haslo)
        uzytkownik.save(using=self._db)
        return uzytkownik



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



# uzytkownik -> nazwa, numer telefonu, login, hasło, adres, mail


# lista ogloszen -> nazwa uzytkownika, nazwa ogloszenia, reszta z powyzej bez opisu


# class lista_ogloszen(models.Model):
#     nazwa_uzytkow = models.CharField(max_length=20, null=False, unique=True)
#     nazwa_ogloszenia = models.CharField(max_length=255, null=False, unique=False)
#     numer_telefonu = models.CharField(max_length=9, null=False, unique=True)
#     login = Uzytkownik.login
#     cena = Ogloszenie.cena
#     opis = Ogloszenie.opis
