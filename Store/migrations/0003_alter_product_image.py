# Generated by Django 4.1.5 on 2023-01-29 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Store", "0002_remove_product_image_thumbnail_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]