from .models import *
from rest_framework import serializers

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"