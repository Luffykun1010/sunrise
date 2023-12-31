# Generated by Django 4.2.4 on 2023-08-09 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=200)),
                ('dep_desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='doctors',
            name='dep_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments'),
        ),
    ]
