# Generated by Django 4.1.1 on 2022-09-26 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
