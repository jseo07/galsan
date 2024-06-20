from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='home'),
    path('logged_index/', views.logged_index, name='logged_index'),
    path('notlogged/', views.notlogged, name='notlogged'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('agree/', views.agree, name='agree'),
    path('redirect_to_blog/', views.redirect_to_blog, name='redirect_to_blog'),
    path('redirect_to_post/', views.redirect_to_post, name='redirect_to_post'),
]