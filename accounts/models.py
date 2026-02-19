from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    full_name = models.CharField(max_length=255, blank=True, verbose_name="ФИО")
    age = models.IntegerField(blank=True, null=True, verbose_name="Возраст")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    education = models.TextField(blank=True, verbose_name="Образование")
    experience = models.TextField(blank=True, verbose_name="Опыт работы")
    skills = models.TextField(blank=True, verbose_name="Навыки")
    desired_position = models.CharField(max_length=255, blank=True, verbose_name="Желаемая должность")
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Ожидаемая зарплата")
    about = models.TextField(blank=True, verbose_name="О себе")

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return self.user.username