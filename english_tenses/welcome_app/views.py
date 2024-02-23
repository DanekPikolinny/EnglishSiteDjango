from django.shortcuts import render

# Create your views here.
def get_welcome_page(request):
    return render(request, 'welcome_app/welcome_index.html')