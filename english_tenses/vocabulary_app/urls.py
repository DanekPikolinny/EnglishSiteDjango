from django.urls import path
from .views import *


urlpatterns = [
    path('', get_welcome_page),
    path('text/', get_main_text_page),
    path('text/<int:text_number>/', get_text_page, name='choosen_text'),
]