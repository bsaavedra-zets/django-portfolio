# Generated by Django 3.2.8 on 2022-02-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20220209_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='exe',
            field=models.FileField(blank=True, upload_to='executable_apps/'),
        ),
    ]