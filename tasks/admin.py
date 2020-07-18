from django.contrib import admin

from tasks import models as task_models

admin.site.register(task_models.Task)
admin.site.register(task_models.Comment)
