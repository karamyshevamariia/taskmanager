from django.db import models


class Task(models.Model):
    tittle = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.tittle
    class Meta:
        verbose_name='задача'
        verbose_name_plural = 'задачи'