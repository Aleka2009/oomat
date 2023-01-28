from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    link = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class License(models.Model):
    image = models.ImageField(upload_to='license_image/')

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'


class LinkType(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

    class Meta:
        verbose_name = 'Тип ссылки'
        verbose_name_plural = 'Тип ссылок'


class Links(models.Model):
    type = models.ForeignKey(LinkType, related_name='links', on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
