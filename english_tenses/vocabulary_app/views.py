from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse
from .models import TextSection


# Create your views here.
def get_welcome_page(request):
    return render(request, 'vocabulary_app/index.html')


def get_all_text(request):
    data = TextSection.objects.all()
    response = {
        'all_texts': data,
    }
    return render(request, 'vocabulary_app/main_text_page.html', context=response)


def get_one_text(request, text_slug):
    text = get_object_or_404(TextSection, slug=text_slug)
    data = {
        'text': text,
    }
    return render(request, 'vocabulary_app/text_page.html', context=data)


def get_one_text_by_num(request, text_number):
    pass


