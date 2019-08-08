from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.get_all),
    path('<int:id>/', views.get_selected, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:id>/edit/', views.update, name='edit'),
    path('download/', views.download_csv, name='download'),
    
]