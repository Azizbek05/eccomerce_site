# Generated by Django 5.0.4 on 2024-04-22 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_t_shirts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_shirts',
            name='price_type',
            field=models.CharField(choices=[('₽', '₽'), ("so'm", "so'm"), ('$', '$')], default="so'm", max_length=10),
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Large')], default='M', max_length=100)),
                ('how', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=100)),
                ('map', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='first.t_shirts')),
            ],
        ),
    ]
