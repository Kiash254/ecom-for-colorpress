# Generated by Django 4.1.5 on 2023-01-29 22:13

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("Store", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image_thumbnail",
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=imagekit.models.fields.ProcessedImageField(upload_to="images/"),
        ),
    ]
