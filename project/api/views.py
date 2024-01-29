from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializer import CustomUserSerializer

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)

  return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
  }

class Register(APIView):
  def post(self, request):
    data = request.data

    if CustomUser.objects.filter(username=data['username']).count() == 0:
      if CustomUser.objects.filter(national_number=data['nationalNumber']).count() == 0:
        CustomUser.objects.create(username=data['username'], password=data['password'], first_name=data['firstName'],\
                                  last_name=data['lastName'], national_number=data['nationalNumber'], birthdate=data['birthdate'],\
                                  phone_number=data['phoneNumber'], address=data['address'], sex=data['sex'], role='patient')
        return Response('0')
      else:
        return Response('.شماره ملی وجود دارد')
    else:
      return Response('.نام کاربری وجود دارد')

class Login(APIView):
  def post(self, request):
    user = CustomUser.objects.filter(username=request.data['username'])
    if user.count() == 1:
      user = user[0]
      if user.password == request.data['password']:
        tmp = get_tokens_for_user(user)
        return Response({'token': tmp, 'role': user.role, 'userId': user.id})

    return Response(".نام کاربری یا رمزعبور اشتباه است")

class UserInfo(APIView):
  def get(self, request):
    user = CustomUser.objects.get(id = request.GET['id'])
    return Response(CustomUserSerializer(user).data)
  
  def post(self, request):
    user = CustomUser.objects.get(id = request.data['id'])
    data = request.data['data']

    user.first_name = data['firstName']
    user.last_name = data['lastName']
    user.password = data['password']
    user.phone_number = data['phoneNumber']
    user.address = data['address']
    user.birthdate = data['birthdate']

    user.save()

    return Response(0)

