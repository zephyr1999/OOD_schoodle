# Generated by Django 2.0.3 on 2018-04-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoodle_app', '0005_auto_20180429_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='content',
        ),
    ]
