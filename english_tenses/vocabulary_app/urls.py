from django.urls import path
from .views import *


urlpatterns = [
    path('', get_welcome_page),
    path('text/', get_main_text_page, name='vocabulary_main_text_page'),
    path('text/<int:text_number>/', get_text_page, name='choosen_text_by_num'),
    path('text/<str:text_title>/', get_text_page_by_title, name='choosen_text_by_title'),
]