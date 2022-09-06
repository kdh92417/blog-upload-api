from django.db import models


# 포스팅 모델
class Posting(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    password = models.CharField(max_length=60)

    class Meta:
        db_table = "postings"
