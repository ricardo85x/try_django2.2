from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Ola mundo</h1>")