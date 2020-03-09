from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Ola mundo</h1>")


def about_page(request):
    return HttpResponse("<h1>About Page</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact Page</h1>")
