from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    tid = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    STATUS_CHOICES = (
        ('Not Started','Not Started'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Not Started')


class Leave_apply(models.Model):
    lid=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    Message=models.TextField()
    STATUS_CHOICES = (
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    )
    status=models.CharField(max_length=50,choices=STATUS_CHOICES, default='Null')

