# Generated by Django 2.2.14 on 2020-07-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.IntegerField(default=0),
        ),
    ]
