# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-09 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actionToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='priority',
            field=models.IntegerField(),
        ),
    ]