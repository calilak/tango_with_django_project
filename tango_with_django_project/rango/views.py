from django.shortcuts import render
from rango.models import Category, Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5] #gets the top 5 most liked categories in descending order
    page_list = Page.objects.order_by('-views')[:5] #gets the top 5 most viewed pages in descending order
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    context_dict = {'name': 'Kalila'}
    return render(request, 'rango/about.html',
                  context = context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        #returns a model or raises a DoesNotExist exception
        category = Category.objects.get(slug=category_name_slug) 

        #returns a list of page objects associated with 'category' or an empty list
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
