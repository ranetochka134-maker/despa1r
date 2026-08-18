from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("architecture", "Архитектура"),
        ("interiors", "Интерьеры"),
        ("concepts", "Концепты"),
    ]

    title = models.CharField("Название проекта", max_length=200)
    category = models.CharField(
        "Категория",
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="architecture",
    )
    year = models.PositiveIntegerField("Год")
    location = models.CharField("Локация", max_length=200, blank=True)
    description = models.TextField("Описание")
    cover = models.ImageField("Обложка", upload_to="projects/covers/")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ContentBlock(models.Model):
    CONTENT_TYPES = [
        ("image", "Изображение"),
        ("video", "Видео"),
        ("text", "Текст"),
        ("pdf", "PDF"),
        ("link", "Ссылка"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="content_blocks",
        verbose_name="Проект",
    )
    content_type = models.CharField(
        "Тип контента",
        max_length=20,
        choices=CONTENT_TYPES,
        default="image",
    )
    title = models.CharField("Заголовок блока", max_length=200, blank=True)
    description = models.TextField("Текст / Описание", blank=True)
    image = models.ImageField(
        "Изображение",
        upload_to="projects/images/",
        blank=True,
        null=True,
    )
    video = models.FileField(
        "Видео",
        upload_to="projects/videos/",
        blank=True,
        null=True,
    )
    file = models.FileField(
        "Файл (PDF)",
        upload_to="projects/files/",
        blank=True,
        null=True,
    )
    url = models.URLField("Ссылка", blank=True)
    order = models.PositiveIntegerField("Порядок отображения", default=0)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Блок контента"
        verbose_name_plural = "Блоки контента"
        ordering = ["order", "created_at"]

    def __str__(self):
        return f"{self.project.title} — {self.get_content_type_display()}"