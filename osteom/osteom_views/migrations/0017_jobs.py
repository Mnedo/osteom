# Generated by Django 3.2.4 on 2021-06-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0016_auto_20210629_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=65, verbose_name='Адрес работы')),
                ('work_time', models.CharField(max_length=50, verbose_name='Время работы')),
                ('phones', models.CharField(max_length=100, verbose_name='Номера телеонов \n (если телефонов >1 делить  ";" без пробелов)')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Место работы',
                'verbose_name_plural': 'Места работы',
            },
        ),
    ]