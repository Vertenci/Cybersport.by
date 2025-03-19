from rest_framework import serializers
from .models import Games


class GamesSerializer(serializers.ModelSerializer):
    icon = serializers.CharField(required=True)

    class Meta:
        model = Games
        fields = '__all__'
