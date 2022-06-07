# Generated by Django 4.0.4 on 2022-06-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_author_descriptionproduct_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='shop.product'),
        ),
    ]
