from django.shortcuts import render
from rest_framework import viewsets, serializers, status
from .models import Attendee, Event
from .serializers import AttendeeSerializer, EventSerializer

class AttendeeView(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Create your views here.
