# Generated by Django 3.1.5 on 2021-01-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210111_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='screenshot',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
