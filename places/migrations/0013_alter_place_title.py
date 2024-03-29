# Generated by Django 4.2.2 on 2023-07-01 12:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0012_alter_image_options_alter_place_description_long_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(
                default=uuid.uuid1, max_length=250, unique=True, verbose_name="Локация"
            ),
        ),
    ]
