from rest_framework import serializers

from core.models import ToDo, User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'user',
            'status',
            'text',
        ]
