# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-13 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lendituser',
            name='name',
        ),
    ]
