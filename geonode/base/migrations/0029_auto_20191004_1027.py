# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-10-04 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_auto_20190911_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='starred',
            field=models.BooleanField(default=False, help_text='a Starred will be added by Admin before publication.', verbose_name='starred'),
        ),
    ]