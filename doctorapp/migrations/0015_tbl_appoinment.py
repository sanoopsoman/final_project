# Generated by Django 4.1.3 on 2023-09-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0014_doctor_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
                ('specialization', models.CharField(max_length=30)),
                ('doctor', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('mob', models.IntegerField()),
            ],
        ),
    ]
