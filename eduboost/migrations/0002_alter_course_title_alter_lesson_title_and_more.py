# Generated by Django 4.2.1 on 2023-06-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduboost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(default='course', max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(default='lesson', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='video', max_length=100),
        ),
    ]
