# Generated by Django 4.0.4 on 2022-04-22 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eHospApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField(auto_created=True, default='')),
                ('FullName', models.CharField(default='', max_length=25)),
                ('Gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=10)),
                ('city', models.CharField(default='', max_length=25)),
                ('State', models.CharField(default='', max_length=25)),
                ('Address', models.TextField(default='', max_length=250)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eHospApp.master')),
            ],
        ),
    ]
