# Generated by Django 5.1.2 on 2024-10-30 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdComment',
        ),
    ]