# Generated by Django 4.0.3 on 2022-03-26 18:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flickboutique', '0031_remove_product_productmanufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='soldBy',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]