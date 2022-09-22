from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
from mywatchlist.models import DaftarMywatchlist

def show_mywatchlist(request):
    data_film_mywatchlist = DaftarMywatchlist.objects.all()
    context = {
        'list_film': data_film_mywatchlist,
        'nama': 'Muhammad Raihan',
        'npm': '2106654643'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = DaftarMywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = DaftarMywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



