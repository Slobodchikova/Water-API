from rest_framework import viewsets
from water.serializers import NewWaterSerializer
from water.models import NewWater


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = NewWater.objects.all().order_by()
    serializer_class = NewWaterSerializer  # Сериализатор для модели