# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-07 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refund', '0006_remove_refund_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='student_id',
            field=models.CharField(default='', max_length=3),
        ),
    ]
