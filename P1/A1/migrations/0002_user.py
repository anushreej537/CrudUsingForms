# Generated by Django 5.0.3 on 2024-03-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empnm', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
