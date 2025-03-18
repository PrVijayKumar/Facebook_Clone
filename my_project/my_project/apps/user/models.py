from django.db import models
import datetime
from django.contrib.auth.models import User


# class PostModel(models.Model):
#     # post_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post_title = models.CharField(max_length=200)
#     post_date = models.DateTimeField(default=datetime.datetime.now)
#     post_content = models.ImageField(upload_to="images/")
    
#     def __str__(self):
#         return self.post_title
