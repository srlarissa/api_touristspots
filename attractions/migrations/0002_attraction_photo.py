# Generated by Django 4.2.7 on 2023-11-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='attraction'),
        ),
    ]
