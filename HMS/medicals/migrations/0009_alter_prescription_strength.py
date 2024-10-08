# Generated by Django 5.0.6 on 2024-07-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicals', '0008_alter_prescription_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='strength',
            field=models.CharField(blank=True, choices=[('50mg', 'Mg 50'), ('100mg', 'Mg 100'), ('200mg', 'Mg 200'), ('500mg', 'Mg 500')], max_length=30, null=True),
        ),
    ]
