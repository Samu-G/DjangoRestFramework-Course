# Generated by Django 5.0.1 on 2024-01-02 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manifactured',
            new_name='Manifacturer',
        ),
    ]
