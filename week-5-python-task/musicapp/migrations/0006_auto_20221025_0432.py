# Generated by Django 3.2.16 on 2022-10-25 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_auto_20221025_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
