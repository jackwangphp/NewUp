from django.db import models

# Create your models here.


class Comic(models.Model):
    name = models.CharField(max_length=64)
    update_date = models.DateField(auto_now=True)


class Chapter(models.Model):
    name = models.CharField(max_length=64)
    create_date = models.DateField(auto_now_add=True)
    url = models.CharField(max_length=225)
    source = models.CharField(max_length=64)
    read = models.BooleanField(default=False)
    comic = models.ForeignKey('Comic', on_delete=models.CASCADE, related_name='chapters')


class Source(models.Model):
    comic = models.ForeignKey('Comic', on_delete=models.CASCADE, related_name='chapters')
    url = models.CharField(max_length=225)
    active = models.BooleanField(default=True)
    select = models.CharField(max_length=24)
