from django.contrib import admin

# Register your models here.

# Altera como será mostrado no Painel Admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',) # cria um filtro, sempre deixar a virgula no final
