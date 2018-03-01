# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='camera_id',
        ),
        migrations.AlterField(
            model_name='image',
            name='date_saved',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_src',
            field=models.URLField(max_length=500),
        ),
    ]
