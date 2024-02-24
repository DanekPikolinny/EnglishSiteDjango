from django.shortcuts import render

# Create your views here.
def get_welcome_page(request):
    return render(request, 'grammary_app/index.html')