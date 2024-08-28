# Generated by Django 5.0.6 on 2024-06-02 16:02

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import users.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(blank=True, max_length=20, null=True)),
                ('temperature', models.CharField(blank=True, max_length=20, null=True)),
                ('blood_pressure', models.CharField(blank=True, max_length=20, null=True)),
                ('triage', models.CharField(blank=True, choices=[('CRITICAL', 'Critical'), ('SEVERE', 'Severe'), ('NORMAL', 'Normal')], default='NORMAL', max_length=20, null=True)),
                ('comments', models.TextField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_id', models.CharField(blank=True, default=users.utils.generate_profile_id, max_length=20, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile_pictures/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])])),
                ('religion', models.CharField(blank=True, choices=[('CHRISTIANITY', 'Christianity'), ('ISLAM', 'Islam')], default='CHRISTIANITY', max_length=255, null=True)),
                ('place_of_birth', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('SINGLE', 'Single'), ('MARRIED', 'Married')], default='SINGLE', max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, choices=[('ASHANTI', 'Ashanti'), ('BONO', 'Bono'), ('BONO_EAST', 'Bono East'), ('AHAFO', 'Ahafo'), ('CENTRAL', 'Central'), ('EASTERN', 'Eastern'), ('GREATER_ACCRA', 'Greater Accra'), ('NORTHERN', 'Northern'), ('SAVANNAH', 'Savannah'), ('NORTH_EAST', 'North East'), ('UPPER_EAST', 'Upper East'), ('UPPER_WEST', 'Upper West'), ('VOLTA', 'Volta'), ('OTI', 'Oti'), ('WESTERN', 'Western'), ('WESTERN_NORTH', 'Western North')], default='EASTERN', max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('kin_name', models.CharField(blank=True, max_length=255, null=True)),
                ('kin_address', models.CharField(blank=True, max_length=255, null=True)),
                ('relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('kin_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('kin_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
