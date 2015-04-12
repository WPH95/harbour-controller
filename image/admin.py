from django.contrib import admin
from image.models import Image
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid', )
    filter_horizontal = ('base_label', 'inherit_label',)
admin.site.register(Image, ImageAdmin)