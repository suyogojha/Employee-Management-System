from django.shortcuts import render
from APP.models import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')


def employee_json(request):
    employees = Employee.objects.all()
    data = [employee.get_data() for employee in employees]
    response = {'data': data}
    return JsonResponse(response)