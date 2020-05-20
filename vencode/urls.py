from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('table/', views.promoter_data_all, name='promoters')
    # path('users/', include('django.contrib.auth.urls')),  # remove this when using allauth
]
