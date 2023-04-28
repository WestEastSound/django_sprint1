from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index.html'),
    path('posts/<int:id>/', views.post_detail, name='detail.html'),
    path('category/<slug:category_slug>/', views.category_posts, name='category.html')
]