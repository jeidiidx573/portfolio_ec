# Generated by Django 2.2.14 on 2020-07-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.IntegerField(default=0, max_length=8),
        ),
    ]
