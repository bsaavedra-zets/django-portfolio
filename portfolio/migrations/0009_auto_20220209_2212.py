# Generated by Django 3.2.8 on 2022-02-10 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_rename_cvdowload_cvdownload'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='ubication',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
