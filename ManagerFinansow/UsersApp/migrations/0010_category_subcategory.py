# Generated by Django 4.0.2 on 2022-12-04 11:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0009_delete_category_delete_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UsersApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.category')),
            ],
        ),
    ]
