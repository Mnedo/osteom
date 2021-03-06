# Generated by Django 3.2.4 on 2021-06-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0010_auto_20210629_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='file',
            field=models.FileField(blank=True, upload_to='file', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_urgent',
            field=models.BooleanField(default=True, verbose_name='Отображать'),
        ),
    ]
