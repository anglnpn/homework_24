
from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson
from utils import NULLABLE


class User(AbstractUser):
    """
    Модель для создания пользователя.
    Создается при регистрации.
    """
    username = None
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='media/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    verification_code = models.CharField(max_length=50, verbose_name='код верификации email', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'пользователь'


class Payments(models.Model):
    payment_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='дата платежа')
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, verbose_name='курс оплаченный')
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, verbose_name='оплаченный урок')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Наличные'), ('transfer', 'Перевод')])

    def __str__(self):
        return f'{self.payment_user} {self.payment_date}'

    class Meta:
        verbose_name = 'платеж'

    
