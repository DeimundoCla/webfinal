# Generated by Django 4.1.4 on 2022-12-15 12:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Posteo",
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
                ("titulo", models.CharField(max_length=60)),
                ("subtitulo", models.CharField(max_length=120)),
                ("fecha_publicacion", models.DateTimeField(auto_now_add=True)),
                ("contenido", ckeditor.fields.RichTextField(blank=True)),
                ("imagen", models.ImageField(upload_to="images/")),
                ("url", models.SlugField(max_length=264, unique=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]