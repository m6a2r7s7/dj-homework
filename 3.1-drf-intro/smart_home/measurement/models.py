from django.db import models

from django.utils import timezone

class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(null=True, max_length=200)

class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    date = models.DateField(default=timezone.now, null=True)