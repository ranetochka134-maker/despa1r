from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    location = models.CharField(max_length=200, blank=True)

    cover = models.ImageField(
        upload_to="projects/covers/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

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
        related_name="content_blocks"
    )

    content_type = models.CharField(
        max_length=20,
        choices=CONTENT_TYPES
    )

    title = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="projects/images/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="projects/videos/",
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to="projects/files/",
        blank=True,
        null=True
    )

    url = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["order", "created_at"]

    def __str__(self):
        return f"{self.project.title} — {self.content_type}"