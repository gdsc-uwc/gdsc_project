# Generated by Django 4.0.3 on 2022-03-16 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flickboutique', '0005_businessinfo_username_customerinfo_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessinfo',
            name='userName',
        ),
        migrations.RemoveField(
            model_name='customerinfo',
            name='userName',
        ),
        migrations.AddField(
            model_name='businessinfo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='customer_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]