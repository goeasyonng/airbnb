# Generated by Django 4.1.4 on 2023-02-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0002_alter_photo_file_alter_video_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.URLField(),
        ),
    ]
