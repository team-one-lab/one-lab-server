# Generated by Django 5.0.2 on 2024-03-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitionMember', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitionmember',
            name='onelab_member_status',
        ),
        migrations.AddField(
            model_name='exhibitionmember',
            name='exhibition_member_status',
            field=models.SmallIntegerField(choices=[(0, '참가'), (1, '종료')], default=0),
        ),
    ]