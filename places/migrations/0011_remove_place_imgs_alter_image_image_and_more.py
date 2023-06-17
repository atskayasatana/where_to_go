# Generated by Django 4.2.2 on 2023-06-17 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0010_alter_image_title"),
    ]

    operations = [
        migrations.RemoveField(model_name="place", name="imgs",),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="", verbose_name="Файл"),
        ),
        migrations.AlterField(
            model_name="image",
            name="place",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.place",
                verbose_name="Локация",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="position_number",
            field=models.IntegerField(
                default=0, verbose_name="Порядковый номер изображения"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="title",
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name="Название изображения",
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=models.TextField(verbose_name="Полное описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(verbose_name="Краткое описание"),
        ),
        migrations.AlterField(
            model_name="place",
            name="latitude",
            field=models.FloatField(verbose_name="Широта"),
        ),
        migrations.AlterField(
            model_name="place",
            name="longtitude",
            field=models.FloatField(verbose_name="Долгота"),
        ),
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Локация"),
        ),
    ]
