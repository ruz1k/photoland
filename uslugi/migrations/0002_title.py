# Generated by Django 2.2.3 on 2019-08-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='media/uslugi')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
