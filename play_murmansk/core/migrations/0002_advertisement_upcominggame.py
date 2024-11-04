# Generated by Django 5.1.2 on 2024-11-04 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='advertisements/', verbose_name='Картинка')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
            },
        ),
        migrations.CreateModel(
            name='UpcomingGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upcoming_games/', verbose_name='Картинка')),
                ('text', models.TextField(verbose_name='Текст')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
            ],
            options={
                'verbose_name': 'Ждем и Верим',
            },
        ),
    ]