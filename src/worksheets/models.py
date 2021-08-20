from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class Quiz(BaseModel):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('название'))
    description = models.TextField(blank=False, null=False, verbose_name=_('описание'))
    date_start = models.DateTimeField(verbose_name=_('дата старта'))
    date_finish = models.DateTimeField(verbose_name=_('дата окончания'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quiz'
        verbose_name = _('Опрос')
        verbose_name_plural = _('Опросы')
        ordering = ('created_at',)


class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('викторина'),
                             related_name='questions')
    question_text = models.CharField(max_length=255, blank=False, null=False, verbose_name=_('текст вопроса'))

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'question'
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')
        ordering = ('created_at',)


class Answer(BaseModel):
    question = models.ForeignKey(Question, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('вопрос'),
                                 related_name='answer')
    answer_text = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('текст ответа'))
    is_right = models.BooleanField(default=False, verbose_name=_('правильный ответ'))
    is_answer_text = models.BooleanField(default=False, verbose_name=_('ответ текстом'))

    def __str__(self):
        return f'{self.question}'

    class Meta:
        db_table = 'answer'
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')
        ordering = ('created_at',)


class Result(BaseModel):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('пользователь'))
    hide_name = models.BooleanField(default=False, verbose_name=_('скрыть имя'))
    first_name = models.CharField(max_length=25, blank=False, null=False, verbose_name=_('имя'))
    second_name = models.CharField(max_length=25, blank=False, null=False, verbose_name=_('фамилия'))
    quiz = models.ForeignKey(Quiz, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('викторина'),
                             related_name='quizzes')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        db_table = 'result'
        verbose_name = _('Результат')
        verbose_name_plural = _('Результаты')
        ordering = ('created_at',)


class ResultAnswer(BaseModel):
    result = models.ForeignKey(Result, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('результат'),
                               related_name='results_answer')
    answer = models.ForeignKey(Answer, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_('ответ'),
                               related_name='answers')
    self_answer_text = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('текст ответа'))

    def __str__(self):
        return f'{self.result}'

    class Meta:
        db_table = 'result_answer'
        verbose_name = _('Результат ответа')
        verbose_name_plural = _('Результаты ответов')
        ordering = ('created_at',)
