# Generated by Django 5.0.3 on 2024-07-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogmodel_created_alter_blogmodel_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]