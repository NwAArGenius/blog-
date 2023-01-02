# Generated by Django 4.1.4 on 2022-12-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('titre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images')),
                ('contenu', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=100)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]