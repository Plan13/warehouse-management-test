# Generated by Django 3.0.2 on 2020-02-03 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20200203_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.SmallIntegerField(default=1)),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Cargo')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Supplier')),
            ],
        ),
    ]
