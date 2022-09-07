from django.db import models


class Posting(models.Model):
    """
    포스팅 모델
    """
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "postings"
