# Generated by Django 4.1 on 2022-08-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empName', models.CharField(max_length=100)),
                ('empSalary', models.IntegerField(default=0)),
                ('empDes', models.CharField(max_length=50)),
                ('empDOJ', models.DateTimeField(verbose_name='Employee Joining Date')),
            ],
        ),
    ]