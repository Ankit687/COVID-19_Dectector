# Generated by Django 2.2.10 on 2020-05-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userXRay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xRay', models.ImageField(upload_to='Images')),
            ],
        ),
    ]