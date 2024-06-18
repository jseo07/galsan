from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('announcement/', views.announcement, name ='announcement'),
    path('post_blog/', views.post_blog, name ='post_blog'),
    
]
