# Generated by Django 3.0.3 on 2020-02-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0009_auto_20200211_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='status',
            field=models.CharField(choices=[('Исполнено', 'Исполнено'), ('В пути', 'В пути')], max_length=10, verbose_name='Статус'),
        ),
    ]
