# Generated by Django 4.0.3 on 2022-03-27 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flickboutique', '0035_alter_customershoppingcart_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
