# Generated by Django 5.0.3 on 2024-05-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0064_productmodel_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='priority',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
