# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_post_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumb',
        ),
    ]