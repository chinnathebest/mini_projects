from rest_framework import serializers
from .models import datas

class datasSerializer(serializers.ModelSerializer):
    class Meta:
        model = datas
        fields = (
            'name','age'
        )