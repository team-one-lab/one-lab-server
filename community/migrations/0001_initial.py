# Generated by Django 5.0.2 on 2024-03-13 10:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
        ('like', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('community_title', models.CharField(max_length=50)),
                ('community_content', models.CharField(max_length=3000)),
                ('post_status', models.CharField(choices=[('1', '자료요청'), ('2', '질문'), ('3', '기타')], default='3', max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_community',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CommunityFile',
            fields=[
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='file.file')),
                ('path', models.ImageField(upload_to='community/%y/%m/d')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='files', to='community.community')),
            ],
            options={
                'db_table': 'tbl_community_file',
            },
        ),
        migrations.CreateModel(
            name='CommunityLike',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='like.like')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='community.community')),
            ],
            options={
                'db_table': 'tbl_community_like',
            },
        ),
    ]
