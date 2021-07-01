# Generated by Django 3.2.4 on 2021-06-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0013_certificate_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Название сертификата')),
                ('content', models.TextField(max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='osteom_views/static/images', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Визитка',
                'verbose_name_plural': 'Визитка',
            },
        ),
    ]
