from django.urls import path
from . import views

urlpatterns = [
    path('', views.records_list),
    path('<int:pk>/', views.record_detail),
    path('dashboard/', views.dashboard_summary),
    path('category-summary/', views.category_summary),
]
