# Generated by Django 4.1.5 on 2023-02-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0013_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='saldo',
            field=models.FloatField(default=0),
        ),
    ]
