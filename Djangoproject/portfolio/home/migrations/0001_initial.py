# Generated by Django 4.1.4 on 2022-12-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
