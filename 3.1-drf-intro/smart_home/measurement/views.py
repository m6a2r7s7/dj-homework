from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class view_sensors(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class view_sensordetail(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class create_sensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def create(self, request, id, name, description):
        Sensor(id=id, name=name, description=description).save()
        return HttpResponse(f"Датчик под номером {id} успешно создан!")


class add_measurement(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request, *args, **kwargs):
        Measurement(*args, **kwargs).save()
        return HttpResponse(f"Температура успешно добавлена!")


class edit_sensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, *args, **kwargs):
        Sensor(*args, **kwargs).save()
        return HttpResponse(f'Успешно изменено!')