# Generated by Django 3.2.4 on 2021-06-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20210624_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shopping_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
