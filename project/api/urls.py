from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', views.Register.as_view(), name='patient_register'),
    path('login/', views.Login.as_view(), name='login'),
    path('calender/', include('doctorsCalender.urls')),
]
