from django.db import models


class Task(models.Model):
    title_1 = models.CharField('Заголовок', max_length=20)
    title_2 = models.TextField("Пояснение")


    def __str__(self):
        return self.title_1


    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
