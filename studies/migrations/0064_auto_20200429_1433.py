# Generated by Django 2.1 on 2020-04-29 18:33

from django.db import migrations
import project.fields.datetime_aware_jsonfield
import studies.models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0063_auto_20200428_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'base_manager_name': 'related_manager', 'ordering': ['-demographic_snapshot__created_at'], 'permissions': (('view_all_response_data_in_analytics', 'View all response data in analytics'),)},
        ),
        migrations.AlterField(
            model_name='study',
            name='metadata',
            field=project.fields.datetime_aware_jsonfield.DateTimeAwareJSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='study',
            name='structure',
            field=project.fields.datetime_aware_jsonfield.DateTimeAwareJSONField(default=studies.models.default_study_structure),
        ),
        migrations.AlterField(
            model_name='studytype',
            name='configuration',
            field=project.fields.datetime_aware_jsonfield.DateTimeAwareJSONField(default=studies.models.default_configuration),
        ),
    ]
