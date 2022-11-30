# Generated by Django 4.1.3 on 2022-11-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('type_of_building', models.CharField(max_length=255)),
                ('count_floor', models.IntegerField(blank=True)),
                ('date', models.DateField()),
                ('center', models.JSONField()),
                ('coordinates', models.JSONField()),
            ],
        ),
    ]