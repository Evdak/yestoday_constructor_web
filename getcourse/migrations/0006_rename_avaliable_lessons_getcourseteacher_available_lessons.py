# Generated by Django 4.1 on 2022-08-15 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getcourse', '0005_getcourseteacher_avaliable_lessons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getcourseteacher',
            old_name='avaliable_lessons',
            new_name='available_lessons',
        ),
    ]