# Generated by Django 3.1.2 on 2020-10-22 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201022_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_verify',
            new_name='email_verified',
        ),
    ]