from water.models import NewWater
from rest_framework import serializers


class NewWaterSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = NewWater
        # Поля, которые мы сериализуем
        fields = ["id", "src", "title", "text"]
