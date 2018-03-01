# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sol', models.IntegerField()),
                ('camera_id', models.IntegerField()),
                ('earth_date', models.DateField()),
                ('img_src', models.CharField(max_length=500)),
                ('date_saved', models.DateField()),
            ],
        ),
    ]
