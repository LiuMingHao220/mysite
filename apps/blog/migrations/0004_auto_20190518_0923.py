# Generated by Django 2.0.7 on 2019-05-18 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190517_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_time'], 'verbose_name': 'article', 'verbose_name_plural': 'article'},
        ),
    ]
