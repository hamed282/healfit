# Generated by Django 5.0.3 on 2024-04-14 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0039_alter_productmodel_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='price',
        ),
    ]