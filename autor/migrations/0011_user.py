# Generated by Django 4.1.5 on 2023-02-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0010_alter_seguir_seguido_alter_seguir_seguidor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguindo', models.ManyToManyField(related_name='seguido_por', through='autor.Seguir', to='autor.user')),
            ],
        ),
    ]
