# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0006_quiz_suggested_house'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]