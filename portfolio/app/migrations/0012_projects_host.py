# Generated by Django 4.0.4 on 2022-06-23 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_projects_img2_alter_projects_img3'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]