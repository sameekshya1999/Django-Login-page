# Generated by Django 5.0 on 2024-01-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0003_userprofile_flag_userprofile_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadedImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="uploaded_images/")),
                ("description", models.TextField()),
            ],
        ),
    ]
