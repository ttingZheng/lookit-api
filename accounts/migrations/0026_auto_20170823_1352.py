# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0025_auto_20170817_1935")]

    operations = [
        migrations.AlterField(
            model_name="demographicdata",
            name="number_of_books",
            field=models.IntegerField(blank=True, default=0),
        )
    ]
