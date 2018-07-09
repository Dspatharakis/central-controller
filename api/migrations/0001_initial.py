# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-06 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(default=0)),
                ('prev_subm', models.IntegerField(default=0)),
                ('prev_rej', models.IntegerField(default=0)),
                ('next_predicted_rr', models.FloatField(default=0)),
            ],
        ),
    ]
