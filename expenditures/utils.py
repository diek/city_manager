from .models import Salary


def calculate_police():
    total = 0.00
    seventy_plus = Salary.objects.filter(department__contains='Police').filter(salary__gte=72510)
    for police_employee in seventy_plus:
        total += police_employee.salary
    return total
