# Generated by Django 2.0.7 on 2019-05-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190518_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modifyed_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
