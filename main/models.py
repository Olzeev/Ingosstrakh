from django.db import models
from datetime import datetime, date

class UserInfo(models.Model):
    username = models.CharField(default="", max_length=30)
    birth_date = models.DateField(default=date.today())
    weight = models.IntegerField(default=0)
    gender = models.BooleanField(default=0) # мужской по дефолту
    message = models.TextField(default="Вы еще не отправляли ни одного отчета")

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "User info"
        verbose_name_plural = "Users info"

class MedicalInfo(models.Model):
    username = models.CharField(max_length=30)
    report_datetime = models.DateTimeField()
    pulse1 = models.IntegerField()
    pulse2 = models.IntegerField()
    preassure1 = models.IntegerField()
    preassure2 = models.IntegerField()
    preassure3 = models.IntegerField()
    preassure4 = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.username} ({self.report_datetime})"

    class Meta:
        verbose_name = "User's medical info"
        verbose_name_plural = "Users' medical info"
