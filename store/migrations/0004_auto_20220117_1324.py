# Generated by Django 3.2.11 on 2022-01-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220117_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name_plural': 'Product Images'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='images/products/default.jpg', help_text='Upload a product image', upload_to='images/products', verbose_name='image'),
        ),
    ]
