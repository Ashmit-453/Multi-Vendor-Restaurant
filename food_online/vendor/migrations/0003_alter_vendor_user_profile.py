# Generated by Django 5.1.1 on 2024-10-11 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
        ('vendor', '0002_rename_vendor_licence_vendor_vendor_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='accounts.userprofile'),
        ),
    ]
