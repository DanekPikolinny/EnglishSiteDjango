from django.urls import path
from .views import *


urlpatterns = [
    path('', get_welcome_page, name='welcome-page'),
    path('text/', get_all_text, name='vocabulary_main_text_page'),
    path('text/<int:text_number>/', get_one_text_by_num, name='choosen_text_by_num'),
    path('text/<slug:text_slug>/', get_one_text, name='choosen_text'),
]