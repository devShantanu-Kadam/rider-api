# Generated by Django 4.2.4 on 2023-08-19 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tour_id',
            new_name='tour',
        ),
    ]
