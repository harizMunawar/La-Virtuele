# Generated by Django 3.1.7 on 2021-06-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.TextField(blank=True, default='', max_length=255, null=True),
        ),
    ]