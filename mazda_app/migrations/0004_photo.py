# Generated by Django 4.0.3 on 2022-04-13 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mazda_app', '0003_alter_car_options_alter_mazda_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mazda_app.car')),
            ],
        ),
    ]
