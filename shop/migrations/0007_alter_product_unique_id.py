# Generated by Django 3.2 on 2021-07-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unique_id',
            field=models.CharField(default='CBaIPNSwyaCn3TD', max_length=50),
        ),
    ]
