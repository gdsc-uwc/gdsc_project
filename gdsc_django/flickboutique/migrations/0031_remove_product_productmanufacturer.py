# Generated by Django 4.0.3 on 2022-03-26 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flickboutique', '0030_remove_product_soldby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productManufacturer',
        ),
    ]