from rest_framework import serializers
from .models import Event,Message
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['host','topic','location','about','date','pic','created','updated']
