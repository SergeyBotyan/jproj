# Generated by Django 3.1.2 on 2020-10-17 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Phone_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_type', models.CharField(max_length=10, verbose_name='Тип телефонного номера')),
                ('description', models.CharField(max_length=10, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_world.persone')),
            ],
        ),
    ]