# Generated by Django 5.1.1 on 2024-10-20 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line2',
            new_name='address_line_2',
        ),
    ]
