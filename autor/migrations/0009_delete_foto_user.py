# Generated by Django 4.1.5 on 2023-02-05 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0008_alter_foto_user_foto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='foto_user',
        ),
    ]
