# Generated by Django 4.1.3 on 2022-12-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UsersApp", "0011_category_scope"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="scope",
            field=models.CharField(
                choices=[("INCOME", "income"), ("EXPENSE", "expense")], max_length=10
            ),
        ),
    ]
