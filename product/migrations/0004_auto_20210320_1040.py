# Generated by Django 3.1.7 on 2021-03-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
