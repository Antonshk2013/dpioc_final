# Generated by Django 4.0.5 on 2022-07-03 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0026_remove_report_image_report_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='subtypereporting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report', to='landing.subtypereporting'),
        ),
        migrations.AddField(
            model_name='subtypereporting',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
