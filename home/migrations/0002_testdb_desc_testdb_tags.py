# Generated by Django 4.2.3 on 2023-07-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="testdb",
            name="desc",
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="testdb",
            name="tags",
            field=models.TextField(null=True),
        ),
    ]