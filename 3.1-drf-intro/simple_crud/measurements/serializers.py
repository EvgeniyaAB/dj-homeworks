from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class MeasurementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"