from django.db import models


class Article(models.Model):

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(max_length=100, verbose_name='Название')
    article = models.ManyToManyField(Article, through='Through_Tag', related_name='tags')

class Through_Tag(models.Model):

    class Meta:
        verbose_name = 'Тематика Статьи'
        verbose_name_plural = 'Тематики Статьи'

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    main = models.BooleanField(blank=True, verbose_name='Основной')