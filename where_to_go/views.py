# views.py

from django.http import HttpResponse

def show_main_page(request):
    text_to_show = 'Здесь будет карта'
    return HttpResponse(text_to_show)