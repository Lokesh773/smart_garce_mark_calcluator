# Generated by Django 3.1.3 on 2021-03-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='email')),
                ('passw', models.CharField(max_length=10, verbose_name='passw')),
                ('role', models.CharField(max_length=50)),
                ('teaches', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
