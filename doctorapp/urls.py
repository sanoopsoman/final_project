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
    path('doctor_profile/<int:id>', views.doctor_profile, name='doctor_profile'),
    path('update_doctor/', views.update_doctor, name='update_doctor'),
    path('update_doctordetail/<int:id>', views.update_doctordetail, name='update_doctordetail'),
    path('patient/', views.patient, name='patient'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('patient_profile/<int:id>', views.patient_profile, name='patient_profile'),
    path('update_patient/', views.update_patient, name='update_patient'),
    path('update_patientdetail/<int:id>', views.update_patientdetail, name='update_patientdetail'),
    path('update_doctor1/<int:id>', views.update_doctor1, name='update_doctor1'),
    path('update_patient1/<int:id>', views.update_patient1, name='update_patient1'),
    path('appoinment/',views.appoinment,name='appoinment'),
    path('patient_data/<int:id>',views.patient_data,name='patient_data'),
    path('user_doctor/',views.user_doctor,name='user_doctor'),
    path('delete_patient/',views.delete_patient,name='delete_patient'),
    path('delete_patient1/<int:id>',views.delete_patient1,name='delete_patient1'),
    path('doctor_profile1/<int:id>',views.doctor_profile1,name='doctor_profile1'),
    path('doctor_update/<int:id>',views.doctor_update,name='doctor_update'),
    path('doctor_update1/<int:id>',views.doctor_update1,name='doctor_update1'),
    path('doctor_delete/<int:id>',views.doctor_delete,name='doctor_delete'),
    path('doctor_patient/',views.doctor_patient,name='doctor_patient'),
    path('doctor_appoinment/',views.doctor_appoinment,name='doctor_appoinment'),
    path('doctor_service/',views.doctor_service,name='doctor_service'),
    path('doctor_patientprofile/<int:id>',views.doctor_patientprofile,name='doctor_patientprofile'),
    path('user_doctorpro/<int:id>',views.user_doctorpro,name='user_doctorpro'),
    path('user_service/',views.user_service,name='user_service'),
    path('user_appoinment/',views.user_appoinment,name='user_appoinment'),
    path('user_contact/',views.user_contact,name='user_contact'),
    path('user_update/<int:id>',views.user_update,name='user_update'),
    path('user_update1/<int:id>', views.user_update1, name='user_update1'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),
    path('admin_service/',views.admin_service,name='admin_service'),
    path('user_booking/',views.user_booking,name='user_booking'),
    path('book_slot/',views.book_slot,name='book_slot'),
    path('user_booking1/<int:id>', views.user_booking1, name='user_booking1'),
    path('user_booking2/', views.user_booking2, name='user_booking2'),
     path('user_booking3/', views.user_booking3, name='user_booking3'),

]
