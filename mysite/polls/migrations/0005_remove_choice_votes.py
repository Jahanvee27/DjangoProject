# Generated by Django 3.2.6 on 2021-09-17 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_choice_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
