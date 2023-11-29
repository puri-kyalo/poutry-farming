# Generated by Django 3.2.23 on 2023-11-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0009_rename_blogsingle_blog_single'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=70)),
                ('message', models.TextField()),
            ],
        ),
    ]
