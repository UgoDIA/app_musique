# Generated by Django 4.2.5 on 2023-09-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio',
            field=models.FileField(upload_to='audio/temp'),
        ),
    ]