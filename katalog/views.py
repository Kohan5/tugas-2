from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Muhammad Raihan',
        'npm': '2106654643'
    }
    return render(request, "katalog.html", context)