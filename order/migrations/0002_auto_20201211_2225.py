# Generated by Django 3.1.3 on 2020-12-11 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='event',
        ),
    ]