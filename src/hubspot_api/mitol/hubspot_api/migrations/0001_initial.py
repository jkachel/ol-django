# Generated by Django 3.2.15 on 2022-10-13 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [  # noqa: RUF012
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [  # noqa: RUF012
        migrations.CreateModel(
            name="HubspotObject",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hubspot_id", models.CharField(max_length=255)),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="hubspotobject",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="hubspot_api_content_object_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="hubspotobject",
            constraint=models.UniqueConstraint(
                fields=("object_id", "content_type"),
                name="hubspot_api_unique_object_id_type",
            ),
        ),
        migrations.AddConstraint(
            model_name="hubspotobject",
            constraint=models.UniqueConstraint(
                fields=("hubspot_id", "content_type"),
                name="hubspot_api_unique_hubspot_id_type",
            ),
        ),
    ]
