from django.db import models

class Attendee(models.Model):
    '''Modelo que guarda la información de los asistentes'''
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    document = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Event(models.Model):
    '''Modelo que guarda la información de los eventos'''
    name = models.CharField(max_length=30)
    date = models.DateTimeField(null=True, blank=True)
    site = models.CharField(max_length=30)
    Attendees = models.ManyToManyField(Attendee)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Create your models here.
