# Generated by Django 3.2.8 on 2022-02-23 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_remove_flag_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificates',
            new_name='Certificate',
        ),
    ]
