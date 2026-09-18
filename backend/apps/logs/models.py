from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Logs(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    mood = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    log_date = models.DateField()
    skills = models.ManyToManyField('skills.Skill', related_name='logs')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title