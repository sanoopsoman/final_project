from django.contrib import admin
from django.urls import path

from doctorapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login2/', views.login2, name='login2'),
    path('register/', views.register, name='register'),
    path('register2/', views.register2, name='register2'),
    path('user2/', views.user2, name='user2'),
    path('doctor/', views.doctor, name='doctor'),
    path('logout/', views.logout, name='logout'),
    path('admin1/', views.admin1, name='admin1'),
    path('doctor_details/', views.doctor_details, name='doctor_details'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_doctor1/', views.add_doctor1, name='add_doctor1'),
    path('delete_doctor/', views.delete_doctor, name='delete_doctor'),
    path('delete_doctor1/<int:id>', views.delete_doctor1, name='delete_doctor1'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
    path('update_doctor/', views.update_doctor, name='update_doctor'),
    path('update_doctordetail/<int:id>', views.update_doctordetail, name='update_doctordetail'),
    path('patient/', views.patient, name='patient'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('patient_profile/<int:id>', views.patient_profile, name='patient_profile'),
    path('update_patient/', views.update_patient, name='update_patient'),
    path('update_patientdetail/<int:id>', views.update_patientdetail, name='update_patientdetail'),
    path('update_doctor1/<int:id>', views.update_doctor1, name='update_doctor1'),
    path('update_patient1/<int:id>', views.update_patient1, name='update_patient1'),
    path('appoinment/',views.appoinment,name='appoinment')

]
