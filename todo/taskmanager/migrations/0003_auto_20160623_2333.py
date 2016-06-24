# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 03:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20160623_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='color',
            field=models.CharField(default='#fff', help_text='Enter the hex color code, like #ccc or #cccccc', max_length=7, validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='taskmanager.Profile', verbose_name='user'),
        ),
    ]
