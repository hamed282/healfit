# Generated by Django 5.0.2 on 2024-03-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_ordermodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemmodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
