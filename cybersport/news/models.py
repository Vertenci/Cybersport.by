from django.db import models

from games.models import Games


class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True)

    title = models.CharField('Название', max_length=150)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField(upload_to='news/news_images/', null=True, blank=True)

    def __str__(self):
        return (f"{self.title} --- {self.game}")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
