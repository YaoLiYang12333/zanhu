# Generated by Django 2.1.5 on 2019-02-14 03:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0004_auto_20190212_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]