# Generated by Django 3.1.5 on 2021-01-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210111_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateField(),
        ),
    ]
