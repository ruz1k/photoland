# Generated by Django 2.2.3 on 2019-08-16 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='primerimage',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
