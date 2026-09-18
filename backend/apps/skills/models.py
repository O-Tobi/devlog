from django.db import models

# Create your models here.

class Skill(models.Model):
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 100, blank= True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name