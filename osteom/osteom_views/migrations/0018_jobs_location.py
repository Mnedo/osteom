# Generated by Django 3.2.4 on 2021-06-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0017_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='location',
            field=models.ImageField(blank=True, upload_to='osteom_views/static/images', verbose_name='Фото местности (не обязательно)'),
        ),
    ]