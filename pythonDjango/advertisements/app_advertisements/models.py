from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price}'

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="red: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.strftime('%H:%M:%S')
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Изображение')
    def img(self):
        if self.image:
            return format_html('<img src="{url}" style="width: 80px; height: 80px" alt="">', url=self.image.url)


class Meta:
    db_table = "advertisements"
