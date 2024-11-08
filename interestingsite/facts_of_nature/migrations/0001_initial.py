# Generated by Django 5.1.1 on 2024-10-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок записи')),
                ('description', models.TextField(verbose_name='Текст записи')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
