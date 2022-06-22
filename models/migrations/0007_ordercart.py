# Generated by Django 4.0.4 on 2022-05-03 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.cart')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.order')),
            ],
        ),
    ]
