# Generated by Django 4.0.4 on 2022-06-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_name_projects_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='img1',
            field=models.ImageField(default='work-3.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='img2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='img3',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]