# Generated by Django 2.0.3 on 2018-04-29 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoodle_app', '0004_auto_20180429_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoodle_app.ContentItemCollection'),
        ),
    ]
