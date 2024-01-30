from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Search_all.as_view(), name='get_all_medicine'),
    path('medicine/', views.Add_medicine.as_view(), name='add_new_medicine'),
    path('amount/', views.Add_medicine_amount.as_view(), name='add_amount_medicine'),
]
