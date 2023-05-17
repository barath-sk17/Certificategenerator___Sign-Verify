# Generated by Django 4.1.6 on 2023-05-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('rollnumber', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=200)),
                ('text', models.FileField(upload_to='')),
                ('public', models.FileField(upload_to='')),
                ('signature', models.FileField(upload_to='')),
            ],
        ),
    ]
