from django.contrib import admin
from .models import Receta

# Register your models here.

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre', 'ingredientes')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    ordering = ('-fecha_creacion',)
    
    fieldsets = (
        (None, {
            'fields': ('nombre', 'imagen')
        }),
        ('Contenido', {
            'fields': ('ingredientes', 'instrucciones')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
