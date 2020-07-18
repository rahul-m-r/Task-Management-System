from django.db import models
from  django.contrib.auth.models import User

from tasks import signals

class Task(models.Model):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, related_name='tasks',on_delete=models.CASCADE, null=True, blank=True)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    end = models.TimeField(auto_now=False, auto_now_add=False)
    day = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    comment = models.TextField()
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Comments_detail", kwargs={"pk": self.pk})

