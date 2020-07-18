from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_admins

def send_notification_mail(sender, instance, **kwargs):
    employee = instance.created_by
    if employee:
        employee_name = employee.username
        task_name = instance.name
        subject = 'New Task'
        message = "{} added new task named {}".format(employee_name, task_name)
        mail_admins(subject, message)

post_save.connect(send_notification_mail, sender='tasks.Task')