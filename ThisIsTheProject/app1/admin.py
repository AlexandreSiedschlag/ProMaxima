from django.contrib import admin
from .models import WebSiteInfo


class InfoAdmin(admin.ModelAdmin):
    list_display = ('Atualizado', 'IP', 'Porto', 'Pais', 'Velocidade', 'Conectados', 'Protocolo', 'Anonimato')


admin.site.register(WebSiteInfo, InfoAdmin)
# Register your models here.
