from django.db import models
# from django.db.models import Lookup, Field
from user.models import User
from django.utils import timezone
import datetime

# Create your models here.
class PostModel(models.Model):
    post_title = models.CharField(max_length=200)
    # post_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="postname")
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="postname")
    post_description = models.TextField()
    post_content = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(default=timezone.now)
    post_updated_date = models.DateTimeField(default=timezone.now)
    post_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post_title


class PostLikes(models.Model):
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return str(self.post_id)
# class NotEqual(Lookup):
#     lookup_name = "ne"

#     def as_sql(self, compiler, connection):
#         lhs, lhs_params = self.process_lhs(compiler, connection)
#         rhs, rhs_params = self.process_rhs(compiler, connection)
#         params = lhs_params + rhs_params
#         return "%s <> %s" % (lhs, rhs), params


# Field.register_lookup(NotEqual)


class PostComments(models.Model):
    comment_desc = models.CharField(max_length=200, null=False)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="pcom")
    com_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters")
    com_date = models.DateTimeField(default=timezone.now)
    com_reply = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name="repliers", null=True)
    com_likes = models.PositiveIntegerField(default=0)
    reply_on_comment = models.PositiveIntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
