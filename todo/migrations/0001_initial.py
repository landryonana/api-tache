# Generated by Django 2.2.28 on 2022-07-18 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('complet', models.BooleanField(default=False)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='category/%Y/%m/%d')),
                ('archived', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('complet', models.BooleanField(default=False)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taches', to='todo.Category', verbose_name='category')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
