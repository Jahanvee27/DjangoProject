# Generated by Django 3.2.6 on 2021-09-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='answer',
            field=models.CharField(default='No answer suggested', max_length=200),
        ),
    ]
