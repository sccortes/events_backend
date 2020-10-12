from django.db import models

class Attendee(models.Model):
    '''Modelo que guarda la información de los asistentes'''
    name = models.CharField(max_length=30, verbose_name='Nombres')
    lastname = models.CharField(max_length=30, verbose_name='Apellidos')
    document = models.CharField(max_length=30, verbose_name='Documento')
    city = models.CharField(max_length=30, verbose_name='Ciudad')
    company_name = models.CharField(max_length=30, verbose_name='Nombre de la compañia')
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Event(models.Model):
    '''Modelo que guarda la información de los eventos'''
    name = models.CharField(max_length=30, verbose_name='Nombre')
    date = models.DateTimeField(verbose_name='Fecha de realización',null=True, blank=True)
    site = models.CharField(max_length=30, verbose_name='Lugar de realización')
    Attendees = models.ManyToManyField(Attendee)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Create your models here.
