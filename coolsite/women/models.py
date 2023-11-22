from django.db import models
import datetime

from django.urls import reverse

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
    slug = models.SlugField(max_length=255, db_index=True, blank=True, default='')

    def get_absolute_url(self):
        return reverse('class', kwargs={'class_slug':self.slug})


    def __str__(self):
        return self.fio


"""
создание записей Students.objects.create(fio="Палий Константин Сергеевич", interesting="плавание, плетение биссером, шахматы, шашки")
выбор всех записей Students.objects.all()
выбор записей по критерию Students.objects.filter(pk=2)
 выбор объектов по фильтру
  https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
Students.objects.filter(is_profcom=1)
выбор одной записи
Students.objects.get(pk=1)
сортировка записей 
Students.objects.order_by('fio')
обратный порядок 
Students.objects.order_by('-fio')
изменить все записи
Students.objects.update(is_profcom=0) 
wd.delete() удаление записи 
"""