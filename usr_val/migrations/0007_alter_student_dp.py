# Generated by Django 3.2.4 on 2021-07-26 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_val', '0006_auto_20210726_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dp',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='students/dp', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', '.jpg', '.jpeg'])]),
        ),
    ]