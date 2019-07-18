from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Category, SubCategory, SubCategoryItem

def index(request):
    categorys = Category.objects.all().order_by('-created_at')
    paginator = Paginator(categorys, 3)

    page = request.GET.get('page')
    categorys = paginator.get_page(page)

    subcatitensall = SubCategoryItem.objects.all().order_by('-created_at')

    paginator = Paginator(subcatitensall, 3)

    page = request.GET.get('page')
    subcatitensall = paginator.get_page(page)

    return render(request, 'frontend/index.html', {'categorys':categorys, 'subcatitensall':subcatitensall})

def etapa2(request, id):
    subcats = SubCategory.objects.filter(category=id).order_by('-created_at')

    paginator = Paginator(subcats, 3)

    page = request.GET.get('page')
    subcats = paginator.get_page(page)
    return render(request, 'frontend/etapa2.html', {'subcats':subcats})


def etapa3(request, id):
    subcatitens = SubCategoryItem.objects.filter(subcategory=id).order_by('-created_at')

    paginator = Paginator(subcatitens, 1)

    page = request.GET.get('page')
    subcatitens = paginator.get_page(page)

    return render(request, 'frontend/etapa3.html', {'subcatitens':subcatitens})