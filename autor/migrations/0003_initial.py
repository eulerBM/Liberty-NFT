# Generated by Django 4.1.5 on 2023-02-02 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autor', '0002_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguidores', to=settings.AUTH_USER_MODEL)),
                ('seguidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguindo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
