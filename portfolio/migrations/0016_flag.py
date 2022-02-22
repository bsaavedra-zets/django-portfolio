# Generated by Django 3.2.8 on 2022-02-22 00:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_skills_icon_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('flag_img', models.FileField(blank=True, null=True, upload_to='flags_img/', validators=[django.core.validators.FileExtensionValidator(['png', 'svg', 'jpg'])])),
            ],
        ),
    ]
