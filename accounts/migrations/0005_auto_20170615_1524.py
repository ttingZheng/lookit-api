# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 15:24
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0004_auto_20170607_1800")]

    operations = [
        migrations.AlterField(
            model_name="demographicdata",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="demographics",
                related_query_name="demographics",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
