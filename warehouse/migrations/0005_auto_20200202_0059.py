# Generated by Django 3.0.2 on 2020-02-01 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_auto_20200202_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='number',
        ),
    ]
