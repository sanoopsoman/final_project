from django.db import models


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
