# Generated by Django 4.2.5 on 2023-09-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_registrationform_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationform',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
