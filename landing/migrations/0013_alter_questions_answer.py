# Generated by Django 4.0.5 on 2022-06-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_alter_statics_metric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.TextField(max_length=2000),
        ),
    ]
