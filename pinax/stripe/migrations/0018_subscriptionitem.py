# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-23 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0017_auto_20181004_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=191, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('metadata', jsonfield.fields.JSONField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Plan')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_stripe.Subscription')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
