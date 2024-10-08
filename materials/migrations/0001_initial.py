# Generated by Django 5.1 on 2024-09-02 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название курса",
                        max_length=100,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Опишите курс",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фотографию курса",
                        null=True,
                        upload_to="materials/photo",
                        verbose_name="Фото",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название урока",
                        max_length=100,
                        verbose_name="Урок",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Опишите урок",
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фотографию урока",
                        null=True,
                        upload_to="materials/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "video",
                    models.URLField(
                        blank=True,
                        help_text="Загрузите видео урока",
                        null=True,
                        verbose_name="Видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
