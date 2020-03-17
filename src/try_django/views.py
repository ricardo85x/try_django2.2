from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Hello there a volta"
    context = { "title": my_title }

    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About US"})


def contact_page(request):
    return render(request, "hello_world.html", {"title": "About Contact US"})


def example_page(request):
    context = { "title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
    # return HttpResponse(template_obj.render(context))