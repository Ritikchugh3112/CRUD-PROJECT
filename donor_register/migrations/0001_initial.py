# Generated by Django 3.2 on 2021-04-27 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicalproblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('BloodGroup', models.CharField(max_length=200)),
                ('medicalproblem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor_register.medicalproblem')),
            ],
        ),
    ]
