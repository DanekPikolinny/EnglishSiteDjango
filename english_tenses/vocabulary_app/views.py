from django.shortcuts import render, HttpResponse


# Create your views here.
def get_text_page(request, text_number):
    return HttpResponse(f"<h1>{text_number} - is your number of choosen text</h1>")