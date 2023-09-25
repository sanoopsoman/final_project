from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from doctorapp.models import tbl_register, tbl_account, doctor_detail, about_us


def index(request):
    obj = about_us.objects.all()
    return render(request, 'index.html', {'res': obj})


def login(request):
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    # obj = about_us.objects.all()

    return render(request, 'register.html')


def register2(request):
    a = tbl_register()

    b = User()
    c = tbl_account()
    a.username = request.POST.get('uname')
    a.first_name = request.POST.get('fname')
    a.last_name = request.POST.get('lname')
    a.email = request.POST.get('email')
    a.address = request.POST.get('address')
    a.mob = request.POST.get('number')
    a.gender = request.POST.get('gender')
    photo = request.FILES['image']
    obj = FileSystemStorage()
    data = obj.save(photo.name, photo)
    x = obj.url(data)
    a.image = x
    b.username = request.POST.get('uname')
    b.first_name = request.POST.get('fname')
    b.last_name = request.POST.get('lname')
    b.email = request.POST.get('email')
    password = request.POST.get('password')
    b.set_password(password)
    cpassword = request.POST.get('cpassword')
    b.set_password(cpassword)
    c.username = request.POST.get('uname')
    c.first_name = request.POST.get('fname')
    c.last_name = request.POST.get('lname')
    c.email = request.POST.get('email')
    c.account_type = "user"
    a.save()
    b.save()
    c.save()

    return render(request, 'register.html')


def add_doctor(request):
    a = doctor_detail()
    b = User()
    c = tbl_account()
    a.username = request.POST.get('uname')
    a.first_name = request.POST.get('fname')
    a.last_name = request.POST.get('lname')
    a.email = request.POST.get('email')
    a.address = request.POST.get('address')
    a.specialization = request.POST.get('special')
    a.experience = request.POST.get('exp')
    a.designation = request.POST.get('desig')
    a.qualification = request.POST.get('qualification')
    a.mob = request.POST.get('number')
    a.gender = request.POST.get('gender')
    photo = request.FILES['image']
    obj = FileSystemStorage()
    data = obj.save(photo.name, photo)
    x = obj.url(data)
    a.image = x
    b.username = request.POST.get('uname')
    b.first_name = request.POST.get('fname')
    b.last_name = request.POST.get('lname')
    b.email = request.POST.get('email')
    password = request.POST.get('password')
    b.set_password(password)
    cpassword = request.POST.get('cpassword')
    b.set_password(cpassword)
    c.username = request.POST.get('uname')
    c.first_name = request.POST.get('fname')
    c.last_name = request.POST.get('lname')
    c.email = request.POST.get('email')
    c.account_type = "doctor"
    a.save()
    b.save()
    c.save()
    return redirect('/admin1')


def add_doctor1(request):
    return render(request, 'add_doctor.html')


def login2(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    print(username, password)
    user1 = authenticate(username=username, password=password)
    print(user1)
    request.session['username'] = username

    if user1 is not None and user1.is_superuser == 1:

        return redirect('/admin1')
    elif user1 is not None and user1.is_superuser == 0:
        x = tbl_account.objects.filter(account_type='doctor')
        return redirect('/doctor')


    else:
        return redirect('/user2')


def user2(request):
    a = request.session['username']
    b = tbl_register.objects.get(username=a)
    return render(request, 'user.html',{'obj':a,'res':b})


def doctor(request):
    a = request.session['username']
    b = doctor_detail.objects.get(username=a)

    return render(request, 'doctor.html', {'obj': a, "x": b})


def admin1(request):
    return render(request, 'admin.html')


def doctor_details(request):
    return render(request, 'doctors_detail.html')


def delete_doctor(request):
    a = doctor_detail.objects.filter(specialization='cardiology')
    return render(request, 'delete_doctor.html', {'obj': a})


def delete_doctor1(request, id):
    a = doctor_detail.objects.get(id=id)
    b = tbl_account.objects.get(username=a.username)
    c = User.objects.get(username=b.username)
    a.delete()
    b.delete()
    c.delete()
    return redirect('/delete_doctor')


def view_doctor(request):
    a = doctor_detail.objects.filter(specialization='cardiology')
    return render(request, 'view_doctor.html', {'obj': a})


def doctor_profile(request):
    return render(request, 'doctor_profile.html')


def update_doctor(request):
    a = doctor_detail.objects.filter(specialization='cardiology')

    return render(request, 'update_doctor.html', {'obj': a})


def update_doctordetail(request, id):
    b = doctor_detail.objects.get(id=id)
    return render(request, 'update_doctordetail.html', {'obj': b})


def patient(request):
    return render(request, 'patient_detail.html')


def view_patient(request):
    a = tbl_register.objects.all()
    print(a)
    return render(request, 'view_patient.html', {'res': a})


def patient_profile(request, id):
    a = tbl_register.objects.get(id=id)
    return render(request, 'patient_profile.html', {'obj': a})


def update_patient(request):
    a = tbl_register.objects.all()
    return render(request, 'update_patient.html', {'obj': a})


def update_patientdetail(request, id):
    a = tbl_register.objects.get(id=id)
    return render(request, 'update_patientdetail.html', {'obj': a})


def update_doctor1(request, id):
    a = doctor_detail.objects.get(id=id)
    b = tbl_account.objects.get(username=a.username)
    c = User.objects.get(username=b.username)
    a.username = request.POST.get('uname')
    a.first_name = request.POST.get('fname')
    a.last_name = request.POST.get('lname')
    a.email = request.POST.get('email')
    a.address = request.POST.get('address')
    a.specialization = request.POST.get('special')
    a.experience = request.POST.get('exp')
    a.designation = request.POST.get('desig')
    a.qualification = request.POST.get('qualification')
    a.mob = request.POST.get('number')
    a.gender = request.POST.get('gender')
    photo = request.FILES['image']
    obj = FileSystemStorage()
    data = obj.save(photo.name, photo)
    x = obj.url(data)
    a.image = x
    b.username = request.POST.get('uname')
    b.first_name = request.POST.get('fname')
    b.last_name = request.POST.get('lname')
    b.email = request.POST.get('email')
    b.account_type = "doctor"
    c.username = request.POST.get('uname')
    c.first_name = request.POST.get('fname')
    c.last_name = request.POST.get('lname')
    c.email = request.POST.get('email')
    password = request.POST.get('password')
    c.set_password(password)
    cpassword = request.POST.get('cpassword')
    c.set_password(cpassword)
    a.save()
    b.save()
    c.save()
    return redirect('/update_doctor')


def update_patient1(request, id):
    a = tbl_register.objects.get(id=id)

    b = User.objects.get(username=a.username)
    c = tbl_account.objects.get(username=b.username)
    a.username = request.POST.get('uname')
    a.first_name = request.POST.get('fname')
    a.last_name = request.POST.get('lname')
    a.email = request.POST.get('email')
    a.address = request.POST.get('address')
    a.mob = request.POST.get('number')
    a.gender = request.POST.get('gender')
    photo = request.FILES['image']
    obj = FileSystemStorage()
    data = obj.save(photo.name, photo)
    x = obj.url(data)
    a.image = x
    b.username = request.POST.get('uname')
    b.first_name = request.POST.get('fname')
    b.last_name = request.POST.get('lname')
    b.email = request.POST.get('email')
    password = request.POST.get('password')
    b.set_password(password)
    cpassword = request.POST.get('cpassword')
    b.set_password(cpassword)
    c.username = request.POST.get('uname')
    c.first_name = request.POST.get('fname')
    c.last_name = request.POST.get('lname')
    c.email = request.POST.get('email')
    c.account_type = "user"
    a.save()
    b.save()
    c.save()

    return redirect('/update_patient')


def appoinment(request):
    return render(request,'appoinment.html')