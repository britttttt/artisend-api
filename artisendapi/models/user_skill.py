from django.db import models
from django.contrib.auth.models import User
from .user_medium import Medium

class Skill(models.Model):
    label = models.CharField(max_length=100)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE, related_name="skills")

    class Meta:
        ordering = ['label']
    
    def __str__(self):
        return self.label
    

class UserSkill(models.Model):

    business = models.ForeignKey('artisendapi.UserBusiness', on_delete=models.CASCADE, related_name='user_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='user_skills')