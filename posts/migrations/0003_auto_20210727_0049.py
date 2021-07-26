# Generated by Django 3.2.4 on 2021-07-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210726_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.AddField(
            model_name='post',
            name='avatar',
            field=models.ImageField(default='../static/defaults/project.png', upload_to='avatars'),
        ),
    ]
