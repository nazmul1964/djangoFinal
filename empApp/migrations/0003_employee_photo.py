# Generated by Django 2.1.7 on 2019-03-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0002_remove_employee_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default='download.jpg', upload_to='images/'),
        ),
    ]
