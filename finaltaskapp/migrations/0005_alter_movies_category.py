# Generated by Django 4.2.2 on 2024-02-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltaskapp', '0004_alter_movies_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='category',
            field=models.CharField(max_length=250),
        ),
    ]
