# Generated by Django 4.0 on 2022-03-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classassignment',
            name='Deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='classassignment',
            name='PublishedAt',
            field=models.DateTimeField(null=True),
        ),
    ]
