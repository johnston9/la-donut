# Generated by Django 3.2.4 on 2021-06-19 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210619_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forsix',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forsix', to='products.product'),
        ),
        migrations.AlterField(
            model_name='size',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='products.product'),
        ),
    ]