# Generated by Django 4.0.6 on 2022-07-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='coin',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='user',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='coin_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='coin_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='total_investment',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='coin_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='order_price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='order_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='order_type',
            field=models.CharField(blank=True, choices=[('B', 'BUY'), ('S', 'SELL')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Portfolio_coin',
        ),
    ]
