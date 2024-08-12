# Generated by Django 5.0.2 on 2024-08-12 22:20

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('published_date', models.DateField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('cover_image', models.URLField(blank=True, null=True)),
                ('page_count', models.PositiveIntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='authors.author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
