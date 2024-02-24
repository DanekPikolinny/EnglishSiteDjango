from django.shortcuts import render, HttpResponse


# Create your views here.
def get_welcome_page(request):
    return render(request, 'vocabulary_app/index.html')


def get_text_page(request, text_number):
    return HttpResponse(f"<h1>{text_number} - is your number of choosen text</h1>")