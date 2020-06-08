from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('find_fantom/', views.fantom_options, name='fantom_find'),
    path('results/', views.find_ven_results, name='find_ven_results'),
    path('results/ven/', views.get_vencodes, name='vencode_df'),
    path('results/e_values/', views.get_e_values, name='e_values'),
    path('task_status/', views.find_ven_status, name='find_ven_status'),
    path('find_ven/', views.upload_file_ven, name='upload_ven'),
    path('test_celery/', views.test_celery, name="test_celery")
    # path('users/', include('django.contrib.auth.urls')),  # remove this when using allauth
]
