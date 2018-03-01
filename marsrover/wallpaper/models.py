# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


# class Rover(models.Model):
#     rover_id = models.IntegerField(primary_key=True)
#     rover_name = models.CharField(max_length=50)
#     landing_date = models.DateField()
#     launch_date = models.DateField()
#     status = models.DateField()
#     max_sol = models.IntegerField()
#     max_date = models.DateField()
#     total_photos = models.IntegerField()


# class Camera(models.Model):
#     camera_id = models.IntegerField(primary_key=True)
#     camera_name = models.CharField(max_length=50)
#     rover_id = models.ForeignKey()
#     camera_fullname = models.CharField(max_length=100)


class Image(models.Model):
    sol = models.IntegerField()
    earth_date = models.DateField()
    img_src = models.URLField(max_length=500)
    date_saved = models.DateTimeField()

    def __str__(self):
        return self.img_src

    def was_saved_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(0, 43200, 0) <= self.date_saved <= now
