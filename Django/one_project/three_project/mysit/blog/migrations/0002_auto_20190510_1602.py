# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-10 08:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 10, 16, 2, 56, 186253)),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='男', max_length=10, verbose_name='用户性别'),
        ),
    ]