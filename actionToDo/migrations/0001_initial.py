# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-09 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='last_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', django_unixdatetimefield.fields.UnixDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ToDo_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('deadline', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('priority', models.IntegerField(max_length=10)),
                ('complete', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Title',
                'verbose_name': 'Title',
            },
        ),
    ]