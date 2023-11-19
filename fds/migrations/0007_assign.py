# Generated by Django 4.2.7 on 2023-11-18 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fds', '0006_cart_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, null=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fds.agents')),
                ('crt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fds.cart')),
            ],
        ),
    ]