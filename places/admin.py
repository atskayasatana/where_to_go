from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import Image, Place
# Register your models here.


class ImageInLine(SortableStackedInline, admin.TabularInline):
    model = Image
    extra = 3
    max_num = 10
    readonly_fields = ('image_preview',)
    fields = ('position_number',  'image', 'image_preview')

    def image_preview(self, obj):
        return format_html('<img src="{}" height=200 width=300 />', obj.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInLine]
    fields = ('title', 'description_short', 'description_long', 'latitude', 'longtitude', 'image_preview')
    readonly_fields = ('image_preview',)
    search_fields = ('title', )

    def image_preview(self, obj):
        return format_html('<img src="{}" height=200 width=300 />', obj.image.url)


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'image_preview')
    raw_id_fields = ('place',)
    fields = ('place', 'position_number', 'image', 'image_preview')
    readonly_fields = ('image_preview',)
    ordering = ['position_number']

    def image_preview(self, obj):
        return format_html('<img src="{}" height=200 width=300 />', obj.image.url)








