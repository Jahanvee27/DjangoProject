# Generated by Django 3.2.6 on 2021-09-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210905_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.CharField(max_length=200),
        ),
    ]
