from rest_framework import serializers
from papp.models import Passengers

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = "__all__"
        