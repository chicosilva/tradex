# Generated by Django 4.2.6 on 2023-10-05 13:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "canceled_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "canceled_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("name", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="images/")),
                ("ean", models.CharField(max_length=13, unique=True)),
                ("min_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("max_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PriceVariation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "canceled_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "canceled_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pricevariations",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]