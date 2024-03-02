from django.contrib import admin
from .models import TextSection

# Register your models here.
@admin.register(TextSection)
class TextSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'rating']
    list_editable = ['text', 'rating']