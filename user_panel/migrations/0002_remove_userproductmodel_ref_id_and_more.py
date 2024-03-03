# Generated by Django 5.0.2 on 2024-03-02 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('user_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproductmodel',
            name='ref_id',
        ),
        migrations.AddField(
            model_name='userproductmodel',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rel_order', to='order.ordermodel'),
            preserve_default=False,
        ),
    ]