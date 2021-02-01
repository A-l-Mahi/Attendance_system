from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path("index", views.index, name="index"),
    path("id_card", views.id_card, name = "id_card"),
    path("contact", views.contact, name = "contact"),
    path("current", views.current, name = "current"),
    path("about", views.about, name = "about"),
   path("aboutt", views.att, name = "att"),
    path("view", views.view, name = "view"),
    path('qr', views.scan, name = "scan"),
]

    