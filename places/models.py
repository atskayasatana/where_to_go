import uuid
from django.db import models
from tinymce.models import HTMLField
from django.conf import settings

# Create your models here.


class Place(models.Model):

    title = models.CharField(max_length=250, verbose_name='Локация', unique=True, default=uuid.uuid1)
    description_short = HTMLField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longtitude = models.FloatField(verbose_name='Долгота')


class Image(models.Model):

    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Локация',
                              related_name='images')
    position_number = models.IntegerField(null=False,
                                          verbose_name='Порядковый номер изображения',
                                          default=0,
                                          blank=False)
    title = models.CharField(max_length=200,
                             null=True,
                             blank=True,
                             verbose_name='Название изображения')

    image = models.ImageField(verbose_name='Файл')

    def save(self, *args, **kwargs):
        self.title = f'{self.position_number} {self.place.title}'
        super(Image, self).save(*args, **kwargs)

    class Meta:
        ordering = ('position_number',)


