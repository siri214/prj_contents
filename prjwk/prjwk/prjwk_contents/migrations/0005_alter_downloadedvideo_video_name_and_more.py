# Generated by Django 4.2.5 on 2023-11-19 17:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prjwk_contents', '0004_remove_downloadedvideo_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadedvideo',
            name='video_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='downloadedvideo',
            unique_together={('user', 'video_name')},
        ),
    ]
