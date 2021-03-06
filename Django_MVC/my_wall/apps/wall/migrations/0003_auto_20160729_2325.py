# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20160729_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pw_hash',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
