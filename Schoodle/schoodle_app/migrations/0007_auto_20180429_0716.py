# Generated by Django 2.0.3 on 2018-04-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoodle_app', '0006_remove_student_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
        migrations.AddField(
            model_name='question',
            name='correctAnswerIndex',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='content',
        ),
        migrations.AddField(
            model_name='instructor',
            name='content',
            field=models.ManyToManyField(to='schoodle_app.ContentItemCollection'),
        ),
    ]
