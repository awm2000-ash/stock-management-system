# Generated by Django 3.0.5 on 2020-10-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mongoapp', '0005_auto_20201002_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
