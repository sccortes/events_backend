from rest_framework import serializers
from .models import Attendee, Event

class AttendeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'