# Generated by Django 4.2.2 on 2024-02-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finaltaskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
