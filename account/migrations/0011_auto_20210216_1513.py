# Generated by Django 3.0.8 on 2021-02-16 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20210213_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]