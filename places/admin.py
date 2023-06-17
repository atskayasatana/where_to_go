from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Image, Place
# Register your models here.

class ImageInLine(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 3
    max_num = 5
    fields = ('position_number',  'image', 'image_preview')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        return mark_safe('<img src="{url}" height="{height}" width="{width}">'.format(
            url=obj.image.url,
            height=200,
            width=300))



@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInLine]
    fields = ('title', 'description_short', 'description_long', 'latitude', 'longtitude', 'image_preview')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        return mark_safe('<img src="{url}" height="{height}" width="{width}">'.format(
            url=obj.image.url,
            height=200,
            width=300))


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title',)
    raw_id_fields = ('place',)
    fields = ('place', 'position_number', 'title', 'image', 'image_preview')
    readonly_fields = ('image_preview',)
    ordering = ['position_number']
    def image_preview(self, obj):
        return mark_safe('<img src="{url}" height="{height}" width="{width}">'.format(
            url=obj.image.url,
            height=200,
            width=300))








