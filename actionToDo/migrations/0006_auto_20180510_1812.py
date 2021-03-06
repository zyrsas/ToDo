# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-10 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actionToDo', '0005_auto_20180509_1158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LastUpdate',
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': 'ToDo List', 'verbose_name_plural': 'ToDo Lists'},
        ),
        migrations.AddField(
            model_name='todolist',
            name='date_of_modification',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='todolist',
            name='id_ToDo',
            field=models.IntegerField(default=0),
        ),
    ]
