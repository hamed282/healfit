# Generated by Django 5.0.2 on 2024-03-13 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderitemmodel_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'ordering': ('paid', '-updated'), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]
