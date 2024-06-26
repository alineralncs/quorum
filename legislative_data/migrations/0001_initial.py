# Generated by Django 5.0.3 on 2024-03-22 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bill",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("primary_sponsor", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Legislator",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "bill_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="legislative_data.bill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VoteResult",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("vote_type", models.IntegerField()),
                (
                    "legislator_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="legislative_data.legislator",
                    ),
                ),
                (
                    "vote_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="legislative_data.vote",
                    ),
                ),
            ],
        ),
    ]
