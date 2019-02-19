# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("studies", "0012_auto_20170705_2012")]

    operations = [
        migrations.AlterField(
            model_name="study",
            name="state",
            field=models.CharField(
                choices=[
                    ("created", "Created"),
                    ("submitted", "Submitted"),
                    ("rejected", "Rejected"),
                    ("retracted", "Retracted"),
                    ("approved", "Approved"),
                    ("active", "Active"),
                    ("paused", "Paused"),
                    ("deactivated", "Deactivated"),
                    ("archived", "Archived"),
                ],
                db_index=True,
                default="created",
                max_length=25,
            ),
        )
    ]
