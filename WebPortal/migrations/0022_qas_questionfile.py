# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-10 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0021_auto_20180410_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='qas',
            name='questionFile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='WebPortal.AudioFile'),
        ),
    ]