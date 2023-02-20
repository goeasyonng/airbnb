# Generated by Django 4.1.5 on 2023-02-20 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0007_room_category_alter_room_amenities_alter_room_owner"),
        ("medias", "0004_rename_descriptions_photo_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="rooms.room",
            ),
        ),
    ]