from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes

from tasks import serializers as task_serializers
from tasks import models as task_models

class TaskList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None, employee=None, format=None):
        task_model = task_models.Task
        if request.user.is_superuser:
            '''
               list tasks by employee,
               list tasks by id or
               list all
            '''
            if employee:
                employee = get_object_or_404(User, username=employee)
                tasks = task_model.objects.filter(created_by=employee)
            elif id:
                tasks = task_model.objects.filter(id=id)
            else:
                tasks = task_model.objects.all()
        else:
            '''
            list task by id or list all
            '''
            if id:
                tasks = task_model.objects.filter(id=id, created_by=request.user)
            else:
                tasks = task_model.objects.filter(created_by=request.user)
        serializer = task_serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''
            create a task
        '''
        serializer = task_serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.created_by = request.user
            task.save()
            response_dict = serializer.data
            response_dict['created_by'] = request.user.username # add task created employee's name
            return Response(response_dict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAdminUser])
def comment(request, task_id):
    task_model = task_models.Task
    task_obj = get_object_or_404(task_model, id=task_id)

    comment_model = task_models.Comment

    if request.method == 'GET':
        '''
        list comments of particular task
        '''
        comments = comment_model.objects.filter(task=task_obj)
        serializer = task_serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        '''
        add a comment
        '''
        comment = request.data.get('comment')
        if comment:
            comment_model.objects.create(task=task_obj, 
                                        comment=comment,
                                        added_by=request.user)
            return Response('comment added', status=status.HTTP_201_CREATED)
    else:
        return Response('failed!!!', status=status.HTTP_400_BAD_REQUEST)
