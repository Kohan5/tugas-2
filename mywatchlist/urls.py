# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_mywatchlist

from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_mywatchlist, name='show_mywatchlist')
]