# Generated by Django 4.1.3 on 2023-10-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0023_tbl_appoinment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='address',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='age',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='booking_type',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='date',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='doctor',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='email',
            field=models.CharField(default=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='fee',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='gender',
            field=models.CharField(default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='id_proof',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='image',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='image1',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='mob',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='name',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='photo',
            field=models.ImageField(default=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='specialization',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='status',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='symtoms',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='time',
            field=models.TimeField(default=True),
        ),
        migrations.AlterField(
            model_name='tbl_appoinment',
            name='username',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
