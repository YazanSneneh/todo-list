from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField(method_name="get_status_display")
    priority_display = serializers.SerializerMethodField(method_name="get_priority_display")

    class Meta:
        model = Todo
        fields = [ "title", "description", "status_display", "priority_display", "due_date"]

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_priority_display(self, obj):
        return obj.get_priority_display()