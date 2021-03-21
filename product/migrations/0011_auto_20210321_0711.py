# Generated by Django 3.1.7 on 2021-03-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productcart_checked_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='Cart', to='product.ProductCart'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='total',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
