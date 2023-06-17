from django.db import models

# Create your models here.
class Place(models.Model):

    title = models.CharField(max_length=250, verbose_name='Локация')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')


class Image(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Локация', related_name='images')
    position_number = models.IntegerField(null=False, verbose_name='Порядковый номер изображения', default=0, blank=False)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название изображения')
    image = models.ImageField(verbose_name='Файл')

    def save(self, *args, **kwargs):
        self.title = f'{self.position_number} {self.place.title}'
        super(Image, self).save(*args, **kwargs)

    def places_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />').format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height

        )
    class Meta:
        ordering = ('position_number',)


