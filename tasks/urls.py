from django.contrib import admin
from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

from tasks import views as task_views

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # get api token
    path('tasks/', task_views.TaskList.as_view(), name='tasks'), # list all tasks
    path('tasks/<int:id>/', task_views.TaskList.as_view(), name='tasks'), # get task from id
    path('tasks/<slug:employee>/', task_views.TaskList.as_view(), name='tasks'), # get all tasks of specific employee

    path('comments/<int:task_id>/', task_views.comment, name='add-comment'), #add and view comments by admin for specific tasks
]
