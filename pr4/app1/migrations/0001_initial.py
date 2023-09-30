# Generated by Django 4.2.5 on 2023-09-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=40)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='registrationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=30)),
                ('profile', models.ImageField(upload_to='images')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]