# Generated by Django 4.1.5 on 2023-01-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
