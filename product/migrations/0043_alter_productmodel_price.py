# Generated by Django 5.0.3 on 2024-04-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0042_alter_productmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]