# Generated by Django 5.1.2 on 2024-12-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_rename_ad_board"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="board/"),
        ),
    ]
