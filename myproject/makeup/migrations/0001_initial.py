# Generated by Django 4.2.11 on 2024-04-19 20:13

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=50)),
                ('location', models.TextField(max_length=200)),
                ('shopphonenumber', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('lastname', models.CharField(max_length=12)),
                ('userphonenumber', models.IntegerField()),
                ('nationalcode', models.IntegerField(null=True)),
                ('gmail', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.BooleanField(null=True)),
                ('age', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skincare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remained', models.IntegerField()),
                ('price', models.IntegerField()),
                ('maincategory', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('aboutproduct', models.TextField(max_length=350)),
                ('expdate', models.DateField()),
                ('productname', models.ForeignKey(max_length=20, on_delete=builtins.any, to='makeup.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Makeup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remained', models.IntegerField()),
                ('price', models.IntegerField()),
                ('maincategory', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('aboutproduct', models.TextField(max_length=350)),
                ('expdate', models.DateField()),
                ('productname', models.ForeignKey(max_length=20, on_delete=builtins.any, to='makeup.shop')),
            ],
        ),
    ]
