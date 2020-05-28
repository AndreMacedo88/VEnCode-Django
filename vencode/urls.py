from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('find_fantom/', views.vencode_fantom_options, name='find_fantom'),
    # path('find_fantom/results/', views.vencode_fantom_results, name='results_fantom'),
    # path('find_fantom/results/ven/', views.get_vencodes, name='vencode_df'),
    path('test_celery/', views.test_celery, name='test_celery')
    # path('users/', include('django.contrib.auth.urls')),  # remove this when using allauth
]
