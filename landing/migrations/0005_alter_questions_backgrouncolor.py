# Generated by Django 4.0.5 on 2022-06-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_alter_questions_backgrouncolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='backgrouncolor',
            field=models.CharField(default='5cc7ff', max_length=20),
        ),
    ]
