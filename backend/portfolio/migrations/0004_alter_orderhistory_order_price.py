# Generated by Django 4.0.6 on 2022-07-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_orderhistory_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='order_price',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
    ]
