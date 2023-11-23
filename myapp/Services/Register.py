import json

from django.http import JsonResponse

from myapp.models import patient


def register_patient(request):
    json_data = json.loads(request.body.decode('utf-8'))
    if json_data is None:
        response = {
            'message': 'patient info was not send successfully',
            'code': '400'
        }
        return JsonResponse(response, status=400)
    patient_entity = patient()
    patient_entity.first_name = json_data['first_name']
    patient_entity.last_name = json_data['last_name']
    patient_entity.birthdate = json_data['birthdate']
    patient_entity.national_id = json_data['national_id']
    patient_entity.phone_number = json_data['phone']
    patient_entity.email = json_data['email']
    patient_entity.save()
