# Generated by Django 5.0.3 on 2024-03-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("legislative_data", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="legislator",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="vote",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]