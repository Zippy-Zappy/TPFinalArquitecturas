# Generated by Django 5.0.3 on 2024-06-13 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='secondary_type',
        ),
    ]