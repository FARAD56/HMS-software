# Generated by Django 5.0.6 on 2024-07-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicals', '0003_alter_prescription_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis',
            field=models.CharField(blank=True, choices=[('Headache', 'Headache'), ('Seizures', 'Seizures'), ('Diabetes', 'Diabetes'), ('Hypertension', 'Hypertension'), ('Depression', 'Depression'), ('Pneumonia', 'Pneumonia'), ('Arthritis', 'Arthritis'), ('Dermathitis', 'Dermathitis'), ('Back Pain', 'Back Pain')], default='Headache', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='type',
            field=models.CharField(blank=True, choices=[('Chronic', 'Chronic'), ('Acute', 'Acute')], default='Acute', max_length=20, null=True),
        ),
    ]
