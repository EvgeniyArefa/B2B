# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0003_auto_20171126_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='periods',
            field=models.ManyToManyField(related_name='_agreement_periods_+', to='agreement.Period'),
        ),
    ]
