# Generated by Django 5.0.3 on 2024-04-11 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_productvariantmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='subcategory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
