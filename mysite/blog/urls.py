from django.urls import path
from blog.views import PostView, post_detail
from blog import views

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
