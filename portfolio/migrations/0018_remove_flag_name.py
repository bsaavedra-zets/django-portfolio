# Generated by Django 3.2.8 on 2022-02-22 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_flag_data_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='name',
        ),
    ]
