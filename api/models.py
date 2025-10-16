from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.CharField(max_length=50,null=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    device = models.TextField(null=True, blank=True)
    message = models.TextField()
    severity = models.CharField(max_length=10,default='low')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.severity}: {self.message[:30]}"