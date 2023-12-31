# Generated by Django 4.1.3 on 2023-08-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0007_delete_add_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('mob', models.IntegerField()),
                ('password', models.IntegerField()),
                ('cpassword', models.IntegerField()),
            ],
        ),
    ]
