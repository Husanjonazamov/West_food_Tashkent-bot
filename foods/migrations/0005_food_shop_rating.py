# Generated by Django 4.2.3 on 2024-05-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_remove_food_image_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='shop_rating',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
