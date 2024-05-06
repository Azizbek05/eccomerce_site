# Generated by Django 5.0.4 on 2024-04-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_alter_t_shirts_price_type_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='t_shirts',
            name='price_type',
            field=models.CharField(choices=[('$', '$'), ('₽', '₽'), ("so'm", "so'm")], default="so'm", max_length=10),
        ),
    ]