# Generated by Django 5.0 on 2024-01-04 19:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0004_uploadedimage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UploadedImage",
        ),
    ]
