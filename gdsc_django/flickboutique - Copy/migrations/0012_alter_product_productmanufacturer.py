# Generated by Django 4.0.3 on 2022-03-17 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flickboutique', '0011_alter_product_productrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productManufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_manufacturer', to='flickboutique.manufacturer'),
        ),
    ]