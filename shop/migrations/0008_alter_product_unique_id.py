# Generated by Django 3.2 on 2021-07-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unique_id',
            field=models.CharField(default='GKYBkwQMVBcW09P', max_length=50, unique=True),
        ),
    ]