# Generated by Django 3.0.7 on 2021-10-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20211016_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comp',
            field=models.BooleanField(default=False),
        ),
    ]
