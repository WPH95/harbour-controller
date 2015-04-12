from django.contrib import admin
from container.models import Container
# Register your models here.
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'engine', 'uid' )
    filter_horizontal = ('base_label',)
admin.site.register(Container, ContainerAdmin)