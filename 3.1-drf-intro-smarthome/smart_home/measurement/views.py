# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from models import Sensor, Measurement
from serializers import SensorChangeSerializer, SensorDetailSerializer, MeasurementSerializer


#получить список датчиков
class SensorsListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



#добавить измерение
class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



#обновить информацию по конкретному датчику
class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


#получить информацию по конкретному датчику
class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer