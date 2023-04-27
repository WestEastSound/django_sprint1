from django.urls import path

from . import views

urlpatterns = [
    path('pages/about/', views.about, name='about.html'),
    path('pages/rules/', views.rules, name='rules.html'),
]