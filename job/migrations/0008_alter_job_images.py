# Generated by Django 5.1.4 on 2024-12-11 19:54

import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='images',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
