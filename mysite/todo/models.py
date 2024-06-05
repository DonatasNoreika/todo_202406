from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    summary = models.TextField(verbose_name="Summary", max_length=2000)
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    user = models.ForeignKey(to=User, verbose_name="User", on_delete=models.CASCADE)
    is_done = models.BooleanField(verbose_name="Is Done", default=False)

    def __str__(self):
        return f"{self.title} ({self.user})"