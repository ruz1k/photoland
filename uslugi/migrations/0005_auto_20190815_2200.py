# Generated by Django 2.2.3 on 2019-08-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0004_auto_20190815_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uslugi',
            name='price',
            field=models.TextField(),
        ),
    ]
