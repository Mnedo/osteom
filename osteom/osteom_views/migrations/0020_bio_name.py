# Generated by Django 3.2.4 on 2021-06-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0019_bio_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='name',
            field=models.CharField(default='', max_length=70, verbose_name='Представить как'),
        ),
    ]
