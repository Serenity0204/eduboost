# Generated by Django 4.2.1 on 2023-06-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_alter_exercise_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
