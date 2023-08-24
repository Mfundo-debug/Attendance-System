from django.shortcuts import render
from .models import Employee
from django_filters.views import FilterView
from .filters import EmployeeFilter
# Create your views here.

class EmployeeListView(FilterView):
    model = Employee
    template_name = 'employee_list.html'
    filterset_class = EmployeeFilter
