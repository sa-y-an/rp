# Generated by Django 3.2.4 on 2021-07-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usr_val', '0007_alter_student_dp'),
        ('posts', '0003_alter_post_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='selected',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected_students', to='usr_val.student'),
        ),
        migrations.AlterField(
            model_name='post',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='applied_students', to='usr_val.Student'),
        ),
    ]