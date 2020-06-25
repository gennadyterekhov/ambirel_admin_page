from django.shortcuts import render, get_object_or_404
from user.models import User
from .models import Category, Product, Attribute, AttributeGroup, Filter, Option


def get_field_names(model):
    fields_obj = model._meta.fields
    fields = []
    for f in fields_obj:
        temp_field = str(f).split('.')[-1]
        if temp_field == 'id' :
            continue
        fields.append(temp_field)
    return fields




def index(request):
    title = 'Index'
    template = 'opencart/index.html'
    context = {'title': title,}
    return render(request, template, context)



def categories(request):
    categories = Category.objects.all()


    title = 'Categories'
    template = 'opencart/categories.html'
    context = {'title': title, 'categories': categories}
    return render(request, template, context)


def products(request):
    title = 'Products'
    template = 'opencart/products.html'
    context = {'title': title,}
    return render(request, template, context)


def attributes(request):
    title = 'Attributes'
    template = 'opencart/attributes.html'
    context = {'title': title,}
    return render(request, template, context)


def filters(request):
    title = 'Filters'
    template = 'opencart/filters.html'
    context = {'title': title,}
    return render(request, template, context)


def options(request):
    title = 'Options'
    template = 'opencart/options.html'
    context = {'title': title,}
    return render(request, template, context)




def create_category(request):
    fields = get_field_names(Category)

    title = 'Creation'
    template = 'opencart/create/category.html'
    context = {'title': title, 'fields': fields,}
    return render(request, template, context)


def create_category_check(request):
    name = request.POST.get('name', False)
    
    category = Category.objects.create(name=name)
    categories = Category.objects.all()
    title = 'Categories'
    template = 'opencart/categories.html'
    context = {'title': title, 'categories': categories}
    return render(request, template, context)


def edit_category(request, id):
    current_obj = Category.objects.get(pk=id)
    fields = get_field_names(Category)

    title = 'Edition'
    template = 'opencart/edit/category.html'
    context = {'title': title, 'fields': fields, "current_obj": current_obj,}
    return render(request, template, context)


def edit_category_check(request):
    name = request.POST.get('name', False)
    cat_id = request.POST.get('id', False)
    

    category = Category.objects.get(pk=int(cat_id))
    category.name = name
    category.save()
    # category = Category.objects.create(name=name)
    categories = Category.objects.all()
    title = 'Categories'
    template = 'opencart/categories.html'
    context = {'title': title, 'categories': categories}
    return render(request, template, context)

