# Generated by Django 3.0 on 2020-05-18 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0011_auto_20190815_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uslugi',
            name='published_date',
        ),
    ]
