# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=60)),
                ('amount', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Placebet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=60)),
                ('amount', models.CharField(max_length=20)),
                ('prediction', models.NullBooleanField(choices=[(True, '0'), (False, '1'), (True, 'x')])),
            ],
        ),
    ]
