from django.contrib import admin
from .models import Image, Place
# Register your models here.

class ImageInLine(admin.TabularInline):
    model = Image
    extra = 3
    max_num = 5
    fields = ('position_number',  'image')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInLine]
    fields = ('title', 'description_short', 'description_long', 'latitude', 'longtitude')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title',)
    raw_id_fields = ('place',)
    fields = ('place', 'position_number', 'title', 'image')


