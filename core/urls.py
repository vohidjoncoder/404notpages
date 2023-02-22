from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('',home),
    path('pages/int:pageid>',category),
    re_path(r'^archive/(?P<year>[0-9]{4})/',archive),
    path("404/",no)
]
