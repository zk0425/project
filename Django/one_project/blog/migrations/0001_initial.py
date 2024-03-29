# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-28 13:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('modifyTime', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章主题')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('publishTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户主键')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='用户名称')),
                ('password', models.CharField(max_length=50, verbose_name='用户密码')),
                ('gender', models.BooleanField(default=True, verbose_name='用户性别')),
                ('age', models.IntegerField(default=18, verbose_name='用户年龄')),
                ('birthday', models.DateTimeField(default=datetime.datetime(2019, 4, 28, 21, 28, 8, 290933))),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
    ]
