# Generated by Django 3.0 on 2022-04-01 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0022_category_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedusers',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]