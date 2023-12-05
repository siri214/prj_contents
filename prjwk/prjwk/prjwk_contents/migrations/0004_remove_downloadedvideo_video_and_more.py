# Generated by Django 4.2.5 on 2023-11-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prjwk_contents', '0003_downloadedvideo_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadedvideo',
            name='video',
        ),
        migrations.AddField(
            model_name='downloadedvideo',
            name='video_name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]