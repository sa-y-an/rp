# Generated by Django 3.2.4 on 2021-07-26 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usr_val', '0009_auto_20210727_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='research_statement',
        ),
        migrations.AddField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(default='default/einstein.jpg', upload_to='avatars'),
        ),
        migrations.CreateModel(
            name='ResearchStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_statement', models.TextField(default=' Please write what inspires you to do Research ', max_length=1000)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usr_val.student')),
            ],
        ),
    ]