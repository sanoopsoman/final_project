from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from doctorapp.models import tbl_register, tbl_account, doctor_detail, about_us, tbl_appoinment


def index(request):
    obj = about_us.objects.all()
    a = doctor_detail.objects.all()
    return render(request, 'index.html', {'res': obj, 'var': a})


def login(request):
    a = about_us.objects.all()
    b = doctor_detail.objects.all()
    return render(request, 'login.html', {'obj': a, 'res': b})


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    b = about_us.objects.all()
    a = doctor_detail.objects.all()

    return render(request, 'register.html', {'obj': a, 'res': b})


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
    a = doctor_detail.objects.all()
    b = about_us.objects.all()
    return render(request, 'add_doctor.html', {'obj': a, 'res': b})


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
    return render(request, 'user.html', {'obj': a, 'res': b})


def doctor(request):
    a = request.session['username']
    b = doctor_detail.objects.get(username=a)
    c = doctor_detail.objects.all()

    return render(request, 'doctor.html', {'obj': a, "x": b, 'var': c})


def admin1(request):
    a = doctor_detail.objects.all()
    return render(request, 'admin.html', {'obj': a})


def doctor_details(request):
    return render(request, 'doctors_detail.html')


def delete_doctor(request):
    a = doctor_detail.objects.filter(specialization='cardiology')
    b = doctor_detail.objects.filter(specialization='neurology')
    c = doctor_detail.objects.filter(specialization='dermatology')
    d = doctor_detail.objects.filter(specialization='children specialist')
    e = doctor_detail.objects.filter(specialization='gynecology')
    return render(request, 'delete_doctor.html', {'obj': a, 'res': b, 'var': c, 'py': d, 'css': e})


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
    b = doctor_detail.objects.filter(specialization='neurology')
    c = doctor_detail.objects.filter(specialization='dermatology')
    d = doctor_detail.objects.filter(specialization='children specialist')
    e = doctor_detail.objects.filter(specialization='gynecology')
    return render(request, 'view_doctor.html', {'obj': a, 'res': b, 'var': c, 'py': d, 'css': e})


def doctor_profile(request, id):
    a = doctor_detail.objects.get(id=id)
    return render(request, 'doctor_profile.html', {'obj': a})


def update_doctor(request):
    a = doctor_detail.objects.filter(specialization='cardiology')
    b = doctor_detail.objects.filter(specialization='neurology')
    c = doctor_detail.objects.filter(specialization='dermatology')
    d = doctor_detail.objects.filter(specialization='children specialist')
    e = doctor_detail.objects.filter(specialization='gynecology')
    f = doctor_detail.objects.all()
    return render(request, 'update_doctor.html', {'obj': a, 'res': b, 'var': c, 'py': d, 'css': e, 'str': f})


def update_doctordetail(request, id):
    b = doctor_detail.objects.get(id=id)
    return render(request, 'update_doctordetail.html', {'obj': b})


def patient(request):
    return render(request, 'patient_detail.html')


def view_patient(request):
    a = tbl_register.objects.all()
    b = doctor_detail.objects.all()
    print(a)
    return render(request, 'view_patient.html', {'res': a, 'obj': b})


def patient_profile(request, id):
    a = tbl_register.objects.get(id=id)
    return render(request, 'patient_profile.html', {'obj': a})


def update_patient(request):
    a = tbl_register.objects.all()
    return render(request, 'update_patient.html', {'obj': a})


def update_patientdetail(request, id):
    a = tbl_register.objects.get(id=id)
    b = doctor_detail.objects.all()
    c = about_us.objects.all()
    return render(request, 'update_patientdetail.html', {'obj': a, 'res': b, 'var': c})


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
    a = doctor_detail.objects.all()
    return render(request, 'appoinment.html', {'obj': a})


def add_appoinment(request):
    a = tbl_appoinment()

    a.name = request.POST.get('name')
    a.email = request.POST.get('email')
    a.address = request.POST.get('address')
    a.specialization = request.POST.get('special')
    a.mob = request.POST.get('number')
    a.gender = request.POST.get('gender')
    photo = request.FILES['image']
    obj = FileSystemStorage()
    data = obj.save(photo.name, photo)
    x = obj.url(data)
    a.image = x
    a.doctor = request.POST.get('dname')
    a.symptoms = request.POST.get('symptoms')
    return redirect('')


def patient_data(request, id):
    b = request.session['username']
    a = tbl_register.objects.get(id=id)
    return render(request, 'patient_biodata.html', {'obj': a, 'res': b})


def user_doctor(request):
    a = doctor_detail.objects.filter(specialization='cardiology')
    b = doctor_detail.objects.filter(specialization='neurology')
    c = doctor_detail.objects.filter(specialization='dermatology')
    d = doctor_detail.objects.filter(specialization='children specialist')
    e = doctor_detail.objects.filter(specialization='gynecology')
    f = request.session['username']
    g = tbl_register.objects.get(username=f)
    return render(request, 'user_doctor.html', {'obj': a, 'res': b, 'var': c, 'py': d, 'css': e, 'str': f, 'java': g})


def delete_patient(request):
    a = tbl_register.objects.all()
    return render(request, 'delete_patient.html', {'obj': a})


def delete_patient1(request, id):
    a = tbl_register.objects.get(id=id)
    b = tbl_account.objects.get(username=a.username)
    c = User.objects.get(username=b.username)
    a.delete()
    b.delete()
    c.delete()
    return redirect('/delete_patient')


def doctor_profile1(request, id):
    a = doctor_detail.objects.get(id=id)
    b = request.session['username']
    return render(request, 'doctor_profile1.html', {'obj': a, 'res': b})


def doctor_update(request, id):
    a = doctor_detail.objects.all()
    b = request.session['username']
    c = doctor_detail.objects.get(id=id)
    # d=User.objects.get(username=c)
    return render(request, 'doctor_update.html', {'obj': a, 'res': b, 'var': c})


def doctor_update1(request, id):
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
    return redirect('/doctor')


def doctor_delete(request, id):
    a = doctor_detail.objects.get(id=id)
    b = tbl_account.objects.get(username=a.username)
    c = User.objects.get(username=b.username)
    a.delete()
    b.delete()
    c.delete()
    return redirect('/')


def doctor_patient(request):
    a = request.session['username']
    b = doctor_detail.objects.get(username=a)
    c = tbl_register.objects.all()
    d = doctor_detail.objects.all()
    return render(request, 'doctor_patient.html', {'obj': a, 'res': b, 'str': c, 'py': d})


def doctor_appoinment(request):
    a = request.session['username']
    b = doctor_detail.objects.get(username=a)
    c = doctor_detail.objects.all()
    return render(request, 'doctor_appoinment.html', {'obj': a, 'res': b, 'str': c})


def doctor_service(request):
    a = about_us.objects.all()
    b = doctor_detail.objects.all()
    c = request.session['username']
    d = doctor_detail.objects.get(username=c)
    return render(request, 'doctor_services.html', {'res': a, 'obj': b, 'var': c, 'str': d})


def doctor_patientprofile(request, id):
    a = request.session['username']
    b = doctor_detail.objects.get(username=a)
    c = tbl_register.objects.get(id=id)
    return render(request, 'doctor_patientprofile.html', {'obj': a, 'res': b, 'str': c})


def user_doctorpro(request, id):
    b = request.session['username']
    c = tbl_register.objects.get(username=b)
    a = doctor_detail.objects.get(id=id)
    return render(request, 'user_doctorpro.html', {'obj': a, 'res': b, 'str': c})


def user_service(request):
    a = about_us.objects.all()
    b = doctor_detail.objects.all()
    c = request.session['username']
    d = tbl_register.objects.get(username=c)
    return render(request, 'user_service.html', {'res': a, 'obj': b, 'var': c, 'str': d})


def user_appoinment(request):
    a = request.session['username']
    b = tbl_register.objects.get(username=a)
    c = doctor_detail.objects.all()
    return render(request, 'user_appoinment.html', {'obj': a, 'res': b, 'str': c})


def user_contact(request):
    return render(request, 'user_contact.html')


def user_update(request, id):
    c = doctor_detail.objects.all()
    b = request.session['username']
    a = tbl_register.objects.get(id=id)
    d = about_us.objects.all()
    e = request.session['username']
    # f=tbl_register.objects.get(username=a)
    return render(request, 'user_update.html', {'obj': a, 'res': b, 'str': c, 'var': d, 'py': e})


def user_update1(request, id):
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
    return redirect('/user2')


def user_delete(request, id):
    a = tbl_register.objects.get(id=id)
    b = tbl_account.objects.get(username=a.username)
    c = User.objects.get(username=b.username)
    a.delete()
    b.delete()
    c.delete()
    return redirect('/')


def admin_service(request):
    a=about_us.objects.all()
    b=doctor_detail.objects.all()
    return render(request, 'admin_service.html',{'obj':a,'res':b})
