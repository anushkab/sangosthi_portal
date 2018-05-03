# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortal', '0007_auto_20170620_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendaudiotrailer',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not scheduled after last save'), (1, 'Scheduled')], default=0),
        ),
        migrations.AlterField(
            model_name='sendaudiotrailer',
            name='recipientAshas',
            field=models.ManyToManyField(blank=True, help_text='You may add additional Ashas here.', to='WebPortal.Asha', verbose_name='Other Ashas'),
        ),
    ]