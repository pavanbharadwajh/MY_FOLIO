# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171231_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.URLField(max_length=255),
        ),
    ]
