# Generated by Django 4.1.7 on 2023-03-23 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phonenumber',
        ),
    ]