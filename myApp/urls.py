from django.urls import path
from . import views

urlpatterns = [

]

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
]