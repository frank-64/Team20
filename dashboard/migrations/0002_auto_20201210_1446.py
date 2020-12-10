# Generated by Django 3.1.4 on 2020-12-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Category',
            field=models.CharField(choices=[('Food', 'Food'), ('Clothing', 'Clothing'), ('Bank Transfer', 'Transfer'), ('Other', 'Other')], default='Other', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Direction',
            field=models.CharField(choices=[('Transaction Out', 'Trans Out'), ('Payee Transfer Out', 'Payee Out'), ('Payee Transfer In', 'Payee In')], default='Transaction Out', max_length=30),
        ),
    ]
