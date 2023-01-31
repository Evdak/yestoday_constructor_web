# Generated by Django 4.1 on 2022-08-15 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('getcourse', '0002_lesson_getcourseteacher_getcoursestudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='getcoursestudent',
            name='hours',
            field=models.FloatField(blank=True, null=True, verbose_name='Куплено часов'),
        ),
        migrations.AlterField(
            model_name='getcoursestudent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='getcoursestudent',
            name='lessons',
            field=models.ManyToManyField(blank=True, to='getcourse.lesson', verbose_name='Уроки'),
        ),
        migrations.AlterField(
            model_name='getcoursestudent',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='getcoursestudent',
            name='surname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='getcoursestudent',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='getcourse.getcourseteacher', verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='getcourseteacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин пользователя'),
        ),
    ]