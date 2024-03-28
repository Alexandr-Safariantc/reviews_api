# Generated by Django 3.2 on 2024-03-22 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0007_Add_review_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('reviewcommentbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='comments', serialize=False, to='reviews.reviewcommentbasemodel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'default_related_name': 'comments',
            },
            bases=('reviews.reviewcommentbasemodel',),
        ),
    ]
