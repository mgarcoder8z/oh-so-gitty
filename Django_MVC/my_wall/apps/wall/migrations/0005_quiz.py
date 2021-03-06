# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0004_user_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=45)),
                ('question2', models.CharField(max_length=45)),
                ('question3', models.CharField(max_length=45)),
                ('question4', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wall.User')),
            ],
            managers=[
                ('quizManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
