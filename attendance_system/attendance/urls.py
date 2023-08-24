from django.urls import path
from .views import EmployeeListView

urlpatterns = [
    path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
]