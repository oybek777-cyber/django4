# Generated by Django 5.0.4 on 2024-04-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kompyuter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kompyuter_name', models.CharField(max_length=50)),
                ('windows_number', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
