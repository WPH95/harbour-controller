from django.contrib import admin
from engine.models import Engine
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port' )
    filter_horizontal = ('base_label', 'inherit_label',)

admin.site.register(Engine, EngineAdmin)