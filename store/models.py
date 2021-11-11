from django.db import models


# Create your models here.
class Kategoria(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    class Meta:
        ordering = ('name')

        def __str__(self):
            return self.name


class Ogloszenie(models.Model):
    opis = models.CharField(max_length=255, null=True, unique=False)
    data_dodania = models.DateTimeField(auto_now_add=True)
    marka = models.CharField(max_length=50, unique=False, null=False)
    model = models.CharField(max_length=50, unique=False, null=False)
    rok = models.CharField(max_length=4, null=False, unique=False)
    cena = models.CharField(max_length=255, null=False, unique=False)
    numer_telefonu = models.CharField(max_length=9, null=False, unique=True)
    miejscowosc = models.CharField(max_length=255, null=True, unique=False)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    wlasciciel = models.ForeignKey("auth.User", on_delete=models.CASCADE)


# uzytkownik -> nazwa, numer telefonu, login, hasło, adres, mail


class Uzytkownik(models.Model):
    nazwa_uzytkow = models.CharField(max_length=20, null=False, unique=True)
    numer_telefonu = models.CharField(max_length=9, null=False, unique=True)
    login = models.CharField(max_length=9, null=False, unique=True)
    haslo = models.CharField(max_length=32, null=False, unique=False)
    email = models.CharField(max_length=32, null=False, unique=True)

    # lista ogloszen -> nazwa uzytkownika, nazwa ogloszenia, reszta z powyzej bez opisu


class lista_ogloszen(models.Model):
    nazwa_uzytkow = models.CharField(max_length=20, null=False, unique=True)
    nazwa_ogloszenia = models.CharField(max_length=255, null=False, unique=False)
    numer_telefonu = models.CharField(max_length=9, null=False, unique=True)
    login = Uzytkownik.login
    email = Uzytkownik.email
