from address.models import AddressField
from django.db import models

from users.models import User, Singer

#--------------------------CHOICES---------------------------
POST_CHOICES = (
    ("HISTORY", "History"),
    ("POST", "Post"),
    ("REELS", "Reels"),
)


# -----------------------------------------MODELS------------------------------------

class MusicModel(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    music_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='music/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.singer} - {self.music_name}"


class PostModel(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    tagging = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tagged_posts', null=True, blank=True)
    music = models.ForeignKey(MusicModel, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=8, choices=POST_CHOICES)
    content_url = models.FileField(max_length=200)
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = AddressField(null=True, blank=True)
    hashtag = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.caption}"

    def has_liked(self, user):
        return self.likes.filter(userID=user).exists()

    @property
    def likes_count(self):
        return self.likes.count()


class LikeModel(models.Model):
    postID = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='likes')
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('postID', 'userID')

    def __str__(self):
        return f"{self.userID} liked post {self.postID.id}"




class CommentModel(models.Model):
    postID = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.userID}'s Comment on Post {self.postID.id}"


class CommentLikeModel(models.Model):
    commentID = models.ForeignKey(CommentModel, on_delete=models.CASCADE, related_name='likes')
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReplyCommentModel(models.Model):
    postID = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    commentID = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reply by {self.userID} to Comment {self.commentID.id}"


class ReplyCommentLikeModel(models.Model):
    reply_commentID = models.ForeignKey(ReplyCommentModel, on_delete=models.CASCADE, related_name='likes')
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

