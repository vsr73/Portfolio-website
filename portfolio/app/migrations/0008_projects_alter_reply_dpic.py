# Generated by Django 4.0.4 on 2022-06-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_reply_dpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('client', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('url', models.URLField(max_length=150)),
                ('details', models.TextField(max_length=200)),
                ('bg', models.ImageField(default='work-3.jpg', upload_to='')),
                ('img1', models.ImageField(default='work-3.jpg', upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('img3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='reply',
            name='dpic',
            field=models.ImageField(default='emoji1.png', upload_to=''),
        ),
    ]
