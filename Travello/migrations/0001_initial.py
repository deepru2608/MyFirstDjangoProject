# Generated by Django 3.0.6 on 2020-05-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationName', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='pics')),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Offer', models.BooleanField(default=False)),
            ],
        ),
    ]