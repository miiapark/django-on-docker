from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(db_column="created", auto_now_add=True, help_text="생성일")
    updated = models.DateTimeField(db_column="updated", auto_now=True, help_text="수정일")

    class Meta:
        abstract = True
