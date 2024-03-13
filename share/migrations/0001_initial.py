# Generated by Django 5.0.2 on 2024-03-13 10:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
        ('like', '0001_initial'),
        ('point', '0001_initial'),
        ('review', '0001_initial'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareLike',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='like.like')),
            ],
            options={
                'db_table': 'tbl_share_like',
            },
        ),
        migrations.CreateModel(
            name='SharePoints',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('points', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='point.point')),
            ],
            options={
                'db_table': 'tbl_share_points',
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('share_title', models.CharField(max_length=30)),
                ('share_content', models.CharField(max_length=2000)),
                ('share_points', models.BigIntegerField(default=1000, null=True)),
                ('share_post_status', models.BooleanField(default=True)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='university.university')),
            ],
            options={
                'db_table': 'tbl_share',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ShareFile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='file.file')),
                ('path', models.ImageField(upload_to='share/%Y/%m/%d')),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='share.share')),
            ],
            options={
                'db_table': 'tbl_share_file',
            },
        ),
        migrations.CreateModel(
            name='ShareReview',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='review.review')),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='share.share')),
            ],
            options={
                'db_table': 'tbl_share_review',
            },
        ),
    ]
