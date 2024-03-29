from django.db import models


class Uczelnia(models.Model):
    nazwa = models.CharField(verbose_name='uczelnia', max_length=30)


class Miasto(models.Model):
    nazwa = models.CharField(verbose_name='miasto', max_length=30)
    kod = models.CharField(max_length=30, help_text="Wpisz kod pocztowy")


class Student(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    uczelnia = models.ForeignKey(Uczelnia, on_delete=models.SET_NULL, null=True)
    miasto = models.ForeignKey(Miasto, on_delete=models.SET_NULL, null=True)
    roks = models.CharField(max_length=3, blank=True, default='')
    dochod = models.DecimalField(max_digits=6, decimal_places=2, default=0)
