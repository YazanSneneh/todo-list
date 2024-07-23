from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
    priority = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
