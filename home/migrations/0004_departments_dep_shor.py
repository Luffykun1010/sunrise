# Generated by Django 4.2.4 on 2023-08-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_departments_dep_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='dep_shor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
