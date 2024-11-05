from django.db import models


class Publication(models.Model):
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображения', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Publication, verbose_name='Публикация', on_delete=models.CASCADE)

    def str(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=50)
    posts = models.ForeignKey(Publication, verbose_name='Публикация', on_delete=models.CASCADE)

