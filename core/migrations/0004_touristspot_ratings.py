# Generated by Django 4.2.7 on 2023-11-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
        ('core', '0003_touristspot_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='ratings',
            field=models.ManyToManyField(to='ratings.rating'),
        ),
    ]