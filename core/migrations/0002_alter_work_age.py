# Generated by Django 4.1.5 on 2023-01-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='age',
            field=models.IntegerField(),
        ),
    ]
