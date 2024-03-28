# Generated by Django 3.2 on 2024-03-20 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_Add_category_and_genre_base_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categorygenrebasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='categories', serialize=False, to='reviews.categorygenrebasemodel')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'default_related_name': 'categories',
            },
            bases=('reviews.categorygenrebasemodel',),
        ),
    ]
