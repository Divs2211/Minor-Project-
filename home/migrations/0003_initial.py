# Generated by Django 4.2.6 on 2023-11-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
