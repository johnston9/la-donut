# Generated by Django 3.2.4 on 2021-06-21 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_orderlineitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='forsix',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]