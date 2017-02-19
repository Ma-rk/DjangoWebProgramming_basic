from django.db import models


class Question(models.Model):
    # region FIELDS
    text = models.CharField(max_length=200)
    create_dt = models.DateTimeField('created date')

    # endregion

    def __str__(self):
        return self.text


class Answer(models.Model):
    # region FIELDS
    question_id = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    num_of_votes = models.IntegerField(default=0)

    # endregion

    def __str__(self):
        return self.answer_text
