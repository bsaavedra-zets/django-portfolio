# Generated by Django 3.2.8 on 2021-12-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvDowload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_portfolio', models.FileField(upload_to='profile_documents/')),
            ],
        ),
    ]
