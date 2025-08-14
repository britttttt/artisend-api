from django.db import models
from django.contrib.auth.models import User

class Medium(models.Model):
    label = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['label']

    def __str__(self):
        return self.label


class UserMedium(models.Model):
    business = models.ForeignKey('artisendapi.UserBusiness', on_delete=models.CASCADE, related_name='user_mediums')
    medium = models.ForeignKey('artisendapi.Medium', on_delete=models.CASCADE, related_name='user_business_mediums')
    class Meta:
        unique_together = ('business', 'medium')

    def __str__(self):
        return f"{self.business} - {self.medium}"