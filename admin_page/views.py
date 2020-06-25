from django.shortcuts import render, get_object_or_404
from user.models import User

# Create your views here.
def index(request):
    title = 'Index'
    template = 'admin_page/index.html'
    context = {'title': title,}
    return render(request, template, context)



def categories(request):
    title = 'Categories'
    template = 'admin_page/categories.html'
    context = {'title': title,}
    return render(request, template, context)


def products(request):
    title = 'Products'
    template = 'admin_page/products.html'
    context = {'title': title,}
    return render(request, template, context)


def attributes(request):
    title = 'Attributes'
    template = 'admin_page/attributes.html'
    context = {'title': title,}
    return render(request, template, context)


def filters(request):
    title = 'Filters'
    template = 'admin_page/filters.html'
    context = {'title': title,}
    return render(request, template, context)


def options(request):
    title = 'Options'
    template = 'admin_page/options.html'
    context = {'title': title,}
    return render(request, template, context)