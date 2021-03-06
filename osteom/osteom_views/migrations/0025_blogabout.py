# Generated by Django 3.2.4 on 2021-07-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0024_delete_backgroundphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Из самых последних', max_length=50, verbose_name='Заголовок')),
                ('bio', models.CharField(max_length=100, verbose_name='Описание')),
                ('vk', models.CharField(blank=True, max_length=1000, verbose_name='Ссылка на вк')),
                ('whatsapp', models.CharField(blank=True, max_length=1000, verbose_name='Whatsapp')),
                ('telegram', models.CharField(blank=True, max_length=1000, verbose_name='Телеграмм')),
            ],
            options={
                'verbose_name': 'Био',
                'verbose_name_plural': 'Био',
            },
        ),
    ]
