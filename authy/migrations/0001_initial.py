# Generated by Django 3.0.7 on 2021-10-11 07:53

import authy.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=80, null=True)),
                ('profile_info', models.TextField(blank=True, max_length=150, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=authy.models.user_directory_path, verbose_name='Picture')),
                ('background', models.ImageField(blank=True, null=True, upload_to=authy.models.user_bg__directory_path, verbose_name='Background')),
                ('favorites', models.ManyToManyField(to='post.Post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='achivement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievement/', verbose_name='Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]