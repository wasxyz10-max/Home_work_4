from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Укажите названия книги')
    description = models.TextField(verbose_name='Укажите описания книги')
    image = models.ImageField(upload_to='imgBook/', verbose_name='Загрузите картинку книги')
    created_date = models.PositiveIntegerField(verbose_name='Укажите дату выхода книги', null=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    viki_bok = models.URLField(verbose_name='Укажите ссылку на википедию', null=True)
    book_files = models.FileField(upload_to='files/', verbose_name='Загрузите файл книги', null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Книга и ее описание'
        verbose_name_plural = 'Книги и их описание'