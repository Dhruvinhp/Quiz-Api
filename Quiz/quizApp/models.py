from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    title = models.CharField(max_length=225, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('quiz')
        verbose_name_plural = _('quizzes')
        ordering = ['id']

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('Type of Question'))
    title = models.CharField(max_length=255, verbose_name=_('TITLE'))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))

    def __str__(self):
        return self.title

class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
