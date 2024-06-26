# Generated by Django 3.2 on 2024-03-21 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_Add_title_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.genre', verbose_name='Жанр')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.title', verbose_name='Произведение')),
            ],
            options={
                'verbose_name': 'Связь жанр-название',
                'verbose_name_plural': 'Связи жанры-названия',
            },
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='titles', through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанр'),
        ),
    ]
