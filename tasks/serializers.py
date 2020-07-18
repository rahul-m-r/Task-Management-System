from django.contrib.auth.models import User

from rest_framework import serializers

from tasks import models as task_models

class TaskSerializer(serializers.ModelSerializer):
    start = serializers.TimeField(format='%H:%M', input_formats=['%H:%M',])
    end = serializers.TimeField(format='%H:%M', input_formats=['%H:%M',])
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = task_models.Task
        fields = ['id','name', 'start', 'end', 'created_by']

class CommentSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = task_models.Comment