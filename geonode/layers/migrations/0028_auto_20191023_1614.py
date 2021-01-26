# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-10-23 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0027_auto_20170801_1228_squashed_0033_auto_20180606_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='abstract_en',
            field=models.TextField(blank=True, help_text='brief narrative summary of the content of the resource(s)', max_length=5000, null=True, verbose_name='abstract'),
        ),
    ]