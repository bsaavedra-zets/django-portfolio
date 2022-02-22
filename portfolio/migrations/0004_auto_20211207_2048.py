# Generated by Django 3.2.8 on 2021-12-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_skills_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AddField(
            model_name='project',
            name='project_img',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
    ]
