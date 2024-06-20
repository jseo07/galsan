from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('announcement/', views.PostListAnnouncement.as_view(), name ='announcement'),
    path('post_blog/', views.post_blog, name ='post_blog'),
    path('meeting_log/', views.PostListMeetingLog.as_view(), name ='meeting_log'),
    path('free_posts/', views.PostListFreePosts.as_view(), name ='free_posts'),
    
]
