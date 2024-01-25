from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import CustomUser
from .models import Appointment

class Search_all(APIView):
  def get(self, request):
    doctors = CustomUser.objects.filter(role = 'doctor')
    data = {}

    for doctor in doctors:
      if doctor.expertise not in data:
        data[doctor.expertise] = {'0': '', '1': '', '2': '', '3': '', '4': ''}
      
      times = doctor.attend_time.split(' ')
      name = doctor.first_name + ' ' + doctor.last_name
      for time in times:
        tmp = time.split('-')
        if data[doctor.expertise][tmp[0]] == '':
          data[doctor.expertise][tmp[0]] = name + ' ' + tmp[1] + ':' + tmp[2]
        else:
          data[doctor.expertise][tmp[0]] += ' / ' + name + ' ' + tmp[1] + ':' + tmp[2]

    
    return Response(data)

  def post(self, request):
    expertise = request.data['expertise']
    if expertise:
      doctors = CustomUser.objects.filter(role = 'doctor', expertise = expertise)
      data = []

      for doctor in doctors:
        data.append({'id': doctor.id, 'name': doctor.first_name + ' ' + doctor.last_name})
      
      return Response(data)
    else:
      return Response([])

class Reserve(APIView):
  def get(self, request):
    id = request.GET['id']
    reserved = Appointment.objects.filter(doctor = id)

    if reserved.count() == 0:
      attend_time = CustomUser.objects.filter(id = id)[0].attend_time.split(' ')
      data = []
      for time in attend_time:
        start = int(time.split('-')[1].split(':')[0])
        end = int(time.split('-')[2].split(':')[0])

        for i in range(end-start):
          data.append({'time': time.split('-')[0] + '-' + str(start) + ':00-' + str(start) + ':15', 'value': False})
          data.append({'time': time.split('-')[0] + '-' + str(start) + ':15-' + str(start) + ':30', 'value': False})
          data.append({'time': time.split('-')[0] + '-' + str(start) + ':30-' + str(start) + ':45', 'value': False})
          data.append({'time': time.split('-')[0] + '-' + str(start) + ':45-' + str(start+1) + ':00', 'value': False})
          start += 1
      
      Appointment.objects.create(doctor = CustomUser.objects.filter(id = id)[0], data = data)
      return Response(data)

    return Response(reserved[0].data)
  
  def post(self, request):
    doctor = CustomUser.objects.filter(id = request.data['id'])[0]
    reserved = Appointment.objects.filter(doctor = doctor)[0]
    
    for item in reserved.data:
      if item['time'] == request.data['time']:
        item['value'] = True
        break
    reserved.save()

    return Response(reserved.data)