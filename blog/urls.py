from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('announcement/', views.PostListAnnouncement.as_view(), name ='announcement'),
    path('post_blog/', views.post_blog, name ='post_blog'),
    path('meeting_log/', views.PostListMeetingLog.as_view(), name ='meeting_log'),
    path('free_posts/', views.PostListFreePosts.as_view(), name ='free_posts'),
    path('edit_post/<str:author>/<str:created_on>/', views.edit_post, name ='edit_post'),
    path('delete_post/<str:author>/<str:created_on>/', views.delete_post, name ='delete_post'),
    path('noaccess/', views.noaccess, name ='noaccess'),
]
