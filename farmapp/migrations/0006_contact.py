# Generated by Django 3.2.23 on 2023-11-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('subject', models.CharField(max_length=70)),
                ('message', models.TextField()),
            ],
        ),
    ]