from django.contrib import admin
from .models import TextSection

# Register your models here.

class RatingFilter(admin.FieldListFilter):
    pass


@admin.register(TextSection)
class TextSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'rating', 'rating_status']
    list_editable = ['text', 'rating']
    search_fields = ['title']
    ordering = ['-rating']
    
    @admin.display(description='STATUS')
    def rating_status(self, text:TextSection):
        if text.rating < 50:
            return 'Bad'
        elif 60 > text.rating >= 50:
            return 'Normally'
        elif 70 > text.rating >= 60:
            return 'Good'
        return 'Great'