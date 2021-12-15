# Django

from django.test import TestCase, Client

# Create your tests here.
from store import models
from store.models import Uzytkownik, Ogloszenie, Kategoria


class pjoter(TestCase):
    def setUp(self):
        self.user = Uzytkownik.objects.create_user(username='Tester', password='Haslo123')
        self.c = Client()
        self.admin = Uzytkownik.objects.create_user(username='TesterAdmin',password='Haslo123',is_staff=True, is_superuser=True)

        Ogloszenie.objects.create(
            opis='PASSAT B5 IGŁA PIERWSZY WLASCICIEL BEZWYPADKOWY BABCIA JEZDZILA DO KOSCIOLA',
            kategoria=Kategoria.objects.create(name='testujacakategoria'),
            wlasciciel=self.user,
            marka='Passat',
            model='B5 1.9TDI',
            rok=1999,
            cena=1000,
            numer_telefonu=123456789,
            miejscowosc='Olsztyn',

        )

    def tearDown(self):
        Uzytkownik.objects.all().delete()
        Ogloszenie.objects.all().delete()
        Kategoria.objects.all().delete()

    def test_uzytkownik_view(self):
        self.c.force_login(self.user)
        response = self.c.get('/uzytkownik/')
        self.assertEqual(response.status_code, 403)

    def test_uzytkownik_view_admin(self):
        self.c.force_login(self.admin)
        response = self.c.get('/uzytkownik/')
        self.assertEqual(response.status_code, 200)

    def test_uzytkownik_view_no_logged(self):
        response = self.c.get('/uzytkownik/')
        self.assertEqual(response.status_code, 403)

    def test_ogloszenie_view(self):
        response = self.c.get('/ogloszenia/')
        self.assertEqual(response.status_code, 200)

    def test_ogloszenie_logged(self):
        self.c.force_login(self.user)
        response = self.c.get('/ogloszenia/')
        self.assertEqual(response.status_code, 200)

    def test_ogloszenie_view_admin(self):
        self.c.force_login(self.admin)
        response = self.c.get('/ogloszenia/')
        self.assertEqual(response.status_code, 200)
