# Generated by Django 5.0.6 on 2024-07-01 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0005_delete_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('banace_after_transaction', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transaction_type', models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Return')], null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='author.useraccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
