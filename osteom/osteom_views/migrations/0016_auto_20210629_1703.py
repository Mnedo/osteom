# Generated by Django 3.2.4 on 2021-06-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0015_remove_bio_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bio',
            options={'verbose_name': 'Визитки', 'verbose_name_plural': 'Визитки'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='file',
            field=models.FileField(blank=True, upload_to='osteom_views/static/files', verbose_name='Файл'),
        ),
    ]
