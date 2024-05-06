# Generated by Django 5.0.4 on 2024-04-22 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_shirts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('character', models.TextField()),
                ('price_type', models.CharField(choices=[('$', '$'), ('₽', '₽'), ("so'm", "so'm")], default="so'm", max_length=10)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.category')),
            ],
        ),
    ]
