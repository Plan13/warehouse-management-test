# Generated by Django 3.0.2 on 2020-02-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20200127_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='status',
            field=models.CharField(choices=[('Исполнено', 'Исполнено'), ('В пути', 'В пути')], default='В пути', max_length=9),
        ),
    ]
