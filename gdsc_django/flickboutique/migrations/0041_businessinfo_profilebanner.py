# Generated by Django 4.0.3 on 2022-03-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flickboutique', '0040_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='profileBanner',
            field=models.ImageField(default='nobanner.png', upload_to=''),
        ),
    ]