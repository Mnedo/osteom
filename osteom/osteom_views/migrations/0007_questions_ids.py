# Generated by Django 3.2.4 on 2021-06-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0006_alter_feedback_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='ids',
            field=models.IntegerField(default=0, verbose_name='Индекс'),
        ),
    ]
