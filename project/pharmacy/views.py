from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MedicineSerializer
from api.models import CustomUser
from .models import Medicine

class Search_all(APIView):
  def get(self, request):
    return Response(MedicineSerializer(Medicine.objects.all(), many=True).data)

class Add_medicine(APIView):
  def post(self, request):
    Medicine.objects.create(name = request.data['name'], dose = request.data['dose'], type = request.data['type'], expire_date = request.data['expireDate'], amount = 0)
    return Response(MedicineSerializer(Medicine.objects.all(), many=True).data)

class Add_medicine_amount(APIView):
  def post(self, request):
    medicine = Medicine.objects.get(name = request.data['name'])
    medicine.amount += int(request.data['count'])
    medicine.save()
    
    return Response(MedicineSerializer(Medicine.objects.all(), many=True).data)