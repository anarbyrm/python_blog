# Generated by Django 4.1.3 on 2022-11-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_post_options_remove_lesson_views_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="views",
            field=models.ManyToManyField(blank=True, null=True, to="blog.ipmodel"),
        ),
        migrations.AlterField(
            model_name="post",
            name="views",
            field=models.ManyToManyField(blank=True, null=True, to="blog.ipmodel"),
        ),
    ]
