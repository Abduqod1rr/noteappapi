from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title=models.CharField(max_length=20,default="no title")
    text=models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    put_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}."

