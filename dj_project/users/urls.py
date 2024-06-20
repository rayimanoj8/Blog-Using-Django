from django.urls import path
from . import views
urlpatterns = [
    path('logout/',views.logout,name='logout')
    # path('', views.home,name="blog-home"),
    # path('about/',views.about,name="Blog-about"),
]