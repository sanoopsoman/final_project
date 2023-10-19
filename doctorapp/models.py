from django.db import models
import datetime

# Create your models here.
class about_us(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    img = models.ImageField(upload_to='gallery')
    cap = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class tbl_register(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    image = models.CharField(max_length=500)
    address = models.TextField()
    mob = models.IntegerField()

    class meta:
        db_user = "register"


class tbl_account(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    account_type = models.CharField(max_length=10)

    class meta:
        db_person = "account"


class doctor_detail(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    specialization = models.CharField(max_length=50)
    experience = models.IntegerField()
    designation = models.CharField(max_length=20)
    qualification = models.CharField(max_length=25)
    gender = models.CharField(max_length=20)
    image = models.CharField(max_length=500)
    address = models.TextField()
    mob = models.IntegerField()

    class meta:
        db_doctor = "doctor"


class tbl_appoinment(models.Model):
    booking_type = models.CharField(max_length=10)
    username=models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=None)
    email = models.CharField(max_length=40)
    specialization = models.CharField(max_length=30)
    doctor = models.CharField(max_length=50,default="none")
    gender = models.CharField(max_length=10)
    image = models.CharField(max_length=500)
    address = models.TextField(default='data')
    # date = models.DateField(default=datetime.datetime.now())
    # time = models.TimeField(default=datetime.datetime.now())
    date = models.CharField(max_length=500,default="none")
    time = models.CharField(max_length=500,default="none")

    symtoms = models.TextField(default='text')
    photo = models.ImageField(upload_to='gallery')
    fee = models.IntegerField(default=True)
    mob = models.IntegerField(default=00)
    status = models.CharField(max_length=20)
    image1 = models.CharField(max_length=500)
    id_proof = models.CharField(max_length=30)


    class meta:
        db_book = "appoinment"


class doctor_availability(models.Model):
    name = models.CharField(max_length=30)
    specialization=models.CharField(max_length=30)
    day = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    fee = models.IntegerField()
    status = models.BooleanField(default=True)

    class meta:
        db_doctor = "doctor_availability"


