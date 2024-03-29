# Generated by Django 5.0.2 on 2024-03-08 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_address', models.CharField(max_length=100)),
                ('last_name_address', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('VAT_number', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('address_complement', models.TextField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('identification_number', models.CharField(max_length=100)),
                ('active_address', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
