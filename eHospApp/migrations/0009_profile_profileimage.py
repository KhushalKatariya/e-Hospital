# Generated by Django 4.0.4 on 2022-04-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eHospApp', '0008_rename_city_profile_city_profile_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ProfileImage',
            field=models.FileField(default='user.png', upload_to='images/users'),
        ),
    ]