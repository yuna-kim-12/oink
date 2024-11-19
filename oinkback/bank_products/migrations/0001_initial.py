# Generated by Django 4.2.16 on 2024-11-18 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField()),
                ('company_code', models.TextField()),
                ('company_name', models.TextField()),
                ('product_code', models.TextField()),
                ('product_name', models.TextField()),
                ('interest_rate', models.FloatField()),
                ('prime_interest_rate', models.FloatField()),
                ('product_link', models.TextField()),
                ('join_period', models.TextField()),
                ('join_period_text', models.TextField()),
                ('join_amount_min', models.IntegerField()),
                ('join_amount_max', models.IntegerField(blank=True, null=True)),
                ('join_amount_text', models.TextField()),
                ('join_way', models.TextField(blank=True, null=True)),
                ('join_member', models.TextField()),
                ('prime_conditions', models.TextField(blank=True, null=True)),
                ('interest_payment', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('join_period', models.IntegerField()),
                ('monthly_amount', models.IntegerField()),
                ('interest_rate', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_bank_products', models.ManyToManyField(related_name='bank_product_users', to='bank_products.bankproducts')),
            ],
        ),
    ]
