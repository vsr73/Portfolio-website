from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('blogs/<str:pk>/',views.blogs,name='blogs'),
    path('bolg/<str:pk>/',views.blogs,name='blog'),
    path('portfolio/<str:pk>',views.portfolio,name='portfolio'),
    path('reply/<str:pk>/',views.replycomment,name='reply'),
    ]