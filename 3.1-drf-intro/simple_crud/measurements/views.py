from rest_framework.viewsets import ModelViewSet

from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerializers, MeasurementSerializers


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers



class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializers
