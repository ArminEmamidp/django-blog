# Generated by Django 4.2.6 on 2023-12-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='posts/images/'),
            preserve_default=False,
        ),
    ]
