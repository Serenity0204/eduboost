# Generated by Django 4.2.1 on 2023-08-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_section_image_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='code_snippet',
            field=models.TextField(blank=True, null=True),
        ),
    ]
