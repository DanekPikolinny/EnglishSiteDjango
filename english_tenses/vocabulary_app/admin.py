from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import TextSection, Author
from django.db.models import Q

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'slug']


class RatingFilter(admin.SimpleListFilter):
    title = 'Rating Filter!'
    parameter_name = 'rating'

    # List for lookups (Filter Interface)
    lst = [
        ('first', 'Low rating'),
        ('second', 'Medium rating'),
        ('third', 'High rating'),
    ]

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return self.lst

    def queryset(self, request: Any, qs: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == 'first':
            return qs.filter(Q(rating__lt=40) & Q(rating__gte=0))
        elif self.value() == 'second':
            return qs.filter(Q(rating__gte=40) & Q(rating__lt=80))
        elif self.value() == 'third':
            return qs.filter(Q(rating__gte=80))


@admin.register(TextSection)
class TextSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'rating', 'author']
    list_editable = ['text', 'rating']
    search_fields = ['title']
    ordering = ['-rating']
    list_filter = [
        RatingFilter,
    ]

    actions = [
        'zero_rating'
    ]
    
    # New attribute of the table
    @admin.display(description='STATUS')
    def rating_status(self, text:TextSection):
        if text.rating < 50:
            return 'Bad'
        elif 60 > text.rating >= 50:
            return 'Normally'
        elif 70 > text.rating >= 60:
            return 'Good'
        return 'Great'
    
    @admin.action(description='Change all rating to zeroes')
    def zero_rating(self, request, qs: QuerySet):
        counter = qs.update(rating=0)
        return self.message_user(request, f'Was changed {counter} entries')