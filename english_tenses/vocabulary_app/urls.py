from django.urls import path
from vocabulary_app import views as vocabulary_views


urlpatterns = [
    path('text/<int:text_number>/', vocabulary_views.get_text_page),
]