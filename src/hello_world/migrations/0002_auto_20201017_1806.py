# Generated by Django 3.1.2 on 2020-10-17 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Phone_Type',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Persone',
        ),
    ]