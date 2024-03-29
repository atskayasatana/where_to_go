# Generated by Django 4.2.2 on 2023-07-01 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0013_alter_place_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.place",
                verbose_name="Локация",
            ),
        ),
    ]
