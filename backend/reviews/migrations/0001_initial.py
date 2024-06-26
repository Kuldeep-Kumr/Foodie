# Generated by Django 4.2.11 on 2024-04-01 19:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('text', models.CharField(max_length=256, verbose_name='Review Text')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Review Date')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]
