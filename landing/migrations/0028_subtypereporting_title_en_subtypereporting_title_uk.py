# Generated by Django 4.0.5 on 2022-07-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0027_report_subtypereporting_subtypereporting_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtypereporting',
            name='title_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='subtypereporting',
            name='title_uk',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
