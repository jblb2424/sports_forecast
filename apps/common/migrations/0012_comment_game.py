# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-25 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_team_league'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Game'),
        ),
    ]
