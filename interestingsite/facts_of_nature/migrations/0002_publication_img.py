# Generated by Django 5.1.1 on 2024-10-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facts_of_nature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]