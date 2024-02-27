from django.shortcuts import render, HttpResponse
from django.urls import reverse


# Create your views here.

texts_data = {
    'titles': ["bayeux", "ilon_Mask", "johny_Depp"],
    'texts': []
}


def get_welcome_page(request):
    return render(request, 'vocabulary_app/index.html')


def get_main_text_page(request):
    data = {
    'titles': ["bayeux", "ilon_Mask", "johny_Depp"],
    'texts': []
    }
    return render(request, 'vocabulary_app/main_text_page.html', context=data)


def get_text_page(request, text_number):
    data = {
        'title': texts_data[text_number]['title'],
        'text': texts_data[text_number]['text']
    }
    return render(request, 'vocabulary_app/text_page.html', context=data)


def get_text_page_by_title(request, text_title):
    title = {
        'title': text_title,
    }
    return render(request, 'vocabulary_app/text_page.html', context=title)