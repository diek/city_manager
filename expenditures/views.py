from django.shortcuts import render

from .utils import calculate_police


def get_police(request):
    police_salary = calculate_police()
    return render(request, 'expenditures/police_salary.html', {'police_salary': police_salary})
