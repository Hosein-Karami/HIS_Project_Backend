from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Search_all.as_view(), name='get_all_doctors_calender'),
    path('appointment/', views.Reserve.as_view(), name='reserve_an_appointment'),
    path('patientlist/', views.PatientList.as_view(), name='get_patient_list'),
]
