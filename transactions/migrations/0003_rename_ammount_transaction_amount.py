# Generated by Django 5.0.6 on 2024-07-01 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_rename_banace_after_transaction_transaction_balance_after_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='ammount',
            new_name='amount',
        ),
    ]
