from django.db import models


class Question(models.Model):
    # region FIELDS
    text = models.CharField(max_length=200)
    create_dt = models.DateTimeField('created date')

    # endregion

    def __str__(self):
        return self.text
