# Generated by Django 3.2.4 on 2021-06-29 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osteom_views', '0007_questions_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='ids',
        ),
    ]