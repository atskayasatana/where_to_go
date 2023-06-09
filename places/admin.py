from django.contrib import admin
from .models import Image, Place
# Register your models here.
admin.site.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = 'title'
