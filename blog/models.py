from django.db import models

# Create your models here.
from django.utils import timezone


class BlogArticle(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    article = models.TextField(verbose_name='文章')
    TAG_CHOICES = (
        ('tech', 'Tech'),
        ('life', 'Life'),
    )
    tag = models.CharField(max_length=5, choices=TAG_CHOICES)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
