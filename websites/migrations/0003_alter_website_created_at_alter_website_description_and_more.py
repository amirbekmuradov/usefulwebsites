# Generated by Django 5.1.5 on 2025-01-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='website',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='website',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Number of Likes'),
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Website Title'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(verbose_name='Website URL'),
        ),
    ]
