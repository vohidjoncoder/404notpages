# Generated by Django 4.1.5 on 2023-01-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('firstname', models.CharField(max_length=111)),
                ('age', models.IntegerField(max_length=250)),
            ],
        ),
    ]
