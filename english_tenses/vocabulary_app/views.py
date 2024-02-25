from django.shortcuts import render, HttpResponse
from django.urls import reverse


# Create your views here.
def get_welcome_page(request):
    return render(request, 'vocabulary_app/index.html')


def get_main_text_page(request):
    redirected_urls_dict = {
        'url1': reverse('choosen_text', args=[1]),
        'url2': reverse('choosen_text', args=[2]),
        'url3': reverse('choosen_text', args=[3]),
    }
    return render(request, 'vocabulary_app/main_text_page.html', context=redirected_urls_dict)


texts_data = {
    1: {
        'title': "Bayeux",
        'text': 1
    },
    2: {
        'title': "Ilon Mask",
        'text': 2
    },
    3: {
        'title': "Johny Depp",
        'text': 3
    }
}


def get_text_page(request, text_number):
    data = {
        'title': texts_data[text_number]['title'],
        'text': texts_data[text_number]['text']
    }
    return render(request, 'vocabulary_app/text_page.html', context=data)