# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0005_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='suggested_house',
            field=models.CharField(default='Null', max_length=45),
            preserve_default=False,
        ),
    ]
