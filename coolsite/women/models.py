from django.db import models
import datetime

#А оно для хранения моделей для представления данных из базы данных
# Create your models here.

dt_now = datetime.datetime.now()

class Students(models.Model):
    fio = models.CharField(max_length=30)
    year = models.TextField(blank=True)
    birthday = models.DateField(default=dt_now)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_money = models.BooleanField(default=True)

