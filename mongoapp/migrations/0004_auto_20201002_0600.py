# Generated by Django 3.0.5 on 2020-10-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mongoapp', '0003_auto_20201001_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20, null=True)),
                ('no_of_items', models.IntegerField(default=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
