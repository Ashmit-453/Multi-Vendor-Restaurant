# Generated by Django 5.1.2 on 2024-10-26 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_vendor_venor_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='venor_slug',
            new_name='vendor_slug',
        ),
    ]
