# Generated by Django 5.0.3 on 2024-04-12 11:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0006_remove_userproductmodel_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproductmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='userproductmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
