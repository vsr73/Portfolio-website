# Generated by Django 4.0.4 on 2022-06-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_skills_skill2_skills_skill3_skills_skill4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill3',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill4',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
