# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0019_merge_20170807_1545")]

    operations = [
        migrations.AlterField(
            model_name="child",
            name="additional_information",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="child",
            name="age_at_birth",
            field=models.CharField(
                choices=[
                    ("na", "Not sure or prefer not to answer"),
                    ("<24", "Under 24 weeks"),
                    ("24", "24 weeks"),
                    ("25", "25 weeks"),
                    ("26", "26 weeks"),
                    ("27", "27 weeks"),
                    ("28", "28 weeks"),
                    ("29", "29 weeks"),
                    ("30", "30 weeks"),
                    ("31", "31 weeks"),
                    ("32", "32 weeks"),
                    ("33", "33 weeks"),
                    ("34", "34 weeks"),
                    ("35", "35 weeks"),
                    ("36", "36 weeks"),
                    ("37", "37 weeks"),
                    ("38", "38 weeks"),
                    ("39", "39 weeks"),
                    ("40>", "40 or more weeks"),
                ],
                max_length=25,
            ),
        ),
    ]
