# Generated by Django 4.0.2 on 2022-02-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='breathing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='cough',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='headache',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='sore_throat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='temp',
            field=models.FloatField(),
        ),
    ]
