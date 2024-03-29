import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    #lists of dictionaries
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/', 'views':50},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/', 'views':20},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/', 'views':100}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views':30},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/', 'views':30},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views':50}
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.orgs/docs/dev/', 'views':8},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org', 'views':20}
    ]

    #a dictionary of dictionaries to define categories of pages
    cats = {'Python': {'pages': python_pages},
         'Django': {'pages': django_pages},
         'Other Frameworks': {'pages': other_pages}}

    #adds each category in the cats dictionary
    for cat, cat_data in cats.items():
        if (cat=='Python'):
            c = add_cat(cat, views=128, likes=64)
        elif (cat=='Django'):
            c = add_cat(cat, views=64, likes=32)
        elif (cat=='Other Frameworks'):
            c = add_cat(cat, views=32, likes=16)
        else:
            c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c,p['title'], p['url'], p['views']) #adds each associated page for that category

    #print out categories added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0] #get_or_create()[0] gives model instance
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()