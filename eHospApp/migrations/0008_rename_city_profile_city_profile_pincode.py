# Generated by Django 4.0.4 on 2022-04-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eHospApp', '0007_alter_profile_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city',
            new_name='City',
        ),
        migrations.AddField(
            model_name='profile',
            name='Pincode',
            field=models.CharField(default='', max_length=6),
        ),
    ]
