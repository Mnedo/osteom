# Generated by Django 3.2.4 on 2021-06-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0005_auto_20210628_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Отображение'),
        ),
    ]