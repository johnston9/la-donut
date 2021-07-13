# Generated by Django 3.2.4 on 2021-07-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forsix',
            name='for12',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='forsix',
            name='for24',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='forsix',
            name='for6',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='large',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='medium',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='small',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]