# Generated by Django 2.2 on 2021-01-31 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_comments_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='feed.Comments'),
        ),
    ]