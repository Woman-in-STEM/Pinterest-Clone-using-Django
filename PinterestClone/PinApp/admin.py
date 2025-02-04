from django.contrib import admin
from .models import Board, Pin

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    list_filter = ('name','user')

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ('title', 'board', 'description')
    search_fields = ('title',)
    list_filter = ('board',)
