# Generated by Django 5.0.6 on 2024-07-08 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
