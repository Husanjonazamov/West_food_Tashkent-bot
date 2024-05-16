# Generated by Django 4.2.3 on 2024-05-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_food_shop_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='img',
            field=models.ImageField(default=1, upload_to='foods/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='shop_rating',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
