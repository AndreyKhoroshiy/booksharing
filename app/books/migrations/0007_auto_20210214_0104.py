# Generated by Django 3.1.6 on 2021-02-14 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210214_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.CharField(max_length=20),
        ),
    ]