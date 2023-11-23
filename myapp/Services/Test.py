from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

JWT_authenticator = JWTAuthentication()


def test(request):
    response = JWT_authenticator.authenticate(request)
    print(response)
    response = {'message': 'hello'}
    return JsonResponse(response)
