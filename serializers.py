from rest_framework import serializers
from .models import Event,Message
from django.contrib.auth.models import User
class EventSerializer(serializers.ModelSerializer):
    host_name = serializers.ReadOnlyField(source='host.username')
    host_id = serializers.ReadOnlyField(source='host.id')
    host_email = serializers.ReadOnlyField(source='host.email')
    
    class Meta:
        model = Event       
        #fields = ['host','topic','location','about','date','pic','created','updated']
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    Event = serializers.PrimaryKeyRelatedField(many=True,
                                                 queryset=Event.objects.all())
    class Meta:
        model = User
        #fields = ['id','username','Event']
        fields = '__all__'
