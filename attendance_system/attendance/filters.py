import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    date_of_birth = django_filters.DateFilter(lookup_expr='icontains')
    date_of_joining = django_filters.DateFilter(lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone', 'address', 'date_of_birth', 'date_of_joining')