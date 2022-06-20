# Generated by Django 4.0.5 on 2022-06-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='foodDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('prepared_at', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodmodule.donor')),
            ],
        ),
    ]
