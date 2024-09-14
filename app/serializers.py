from rest_framework import serializers

from .models import ModelTask


class ModelTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTask
        fields = "__all__"
