from typing import List

from accounts.services import UserService
from common.exceptions import ObjectNotFoundException, RequiredObjectException
from worksheets.models import *


class QuizService:
    model = Quiz

    @classmethod
    def get_quiz(cls, **filters) -> Quiz:
        """
            Getting one quiz
        """
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Quiz not found')

    @classmethod
    def filter_quiz(cls, **filters) -> List[Quiz]:
        """
            Getting a list of quizzes
        """
        return cls.model.objects.filter(**filters)


class QuestionService:
    model = Question

    @classmethod
    def get_question(cls, **filters) -> Question:
        """
            Getting one question
        """
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Question not found')

    @classmethod
    def filter_question(cls, **filters) -> List[Question]:
        """
            Getting a list of questions
        """
        return cls.model.objects.filter(**filters)


class AnswerService:
    model = Answer

    @classmethod
    def get_answer(cls, **filters) -> Answer:
        """
            Getting one answer
        """
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Answer not found')

    @classmethod
    def filter_answer(cls, **filters) -> List[Answer]:
        """
            Getting a list of answers
        """
        return cls.model.objects.filter(**filters)


class ResultService:
    model = Result

    @classmethod
    def create_result(cls, hide: bool, f_name: str, s_name: str, quiz: Quiz,
                      answers: List[ResultAnswer], user: User) -> Result:
        found_user = UserService.get_user(id=user.pk)
        stars = '*' * 6
        if hide:
            f_name = f_name[:1] + stars
            s_name = s_name[:1] + stars
        new_result = cls.model.objects.create(user=found_user,
                                              hide_name=hide,
                                              first_name=f_name,
                                              second_name=s_name,
                                              quiz=quiz)
        questions = QuestionService.filter_question(quiz=quiz)
        questions_count = questions.count()
        ResultAnswerService.create_list_result_answer(result=new_result,
                                                      answers=answers,
                                                      counts=questions_count)
        return new_result

    @classmethod
    def get_result(cls, **filters) -> Result:
        """
            Getting one result
        """
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Result not found')

    @classmethod
    def filter_result(cls, **filters) -> List[Result]:
        """
            Getting a list of result
        """
        return cls.model.objects.filter(**filters)


class ResultAnswerService:
    model = ResultAnswer

    @classmethod
    def _create_result_answer(cls, answer_text: str, result: Result, answer: Answer):
        """
            Creating a result answer
        """
        return cls.model.objects.create(result=result,
                                        answer=answer,
                                        self_answer_text=answer_text)

    @classmethod
    def create_list_result_answer(cls, result: Result, answers: List[ResultAnswer], counts: int):
        """
            Creating a list of results answers
        """
        if counts != len(answers):
            raise RequiredObjectException('You must answer all questions')
        for answer_item in answers:
            if answer_item.get('answer').is_right:
                cls._create_result_answer(answer_text=answer_item.get('answer').answer_text,
                                          result=result,
                                          answer=answer_item.get('answer'))
            elif answer_item.get('answer').is_answer_text:
                cls._create_result_answer(answer_text=answer_item.get('self_answer_text'),
                                          result=result,
                                          answer=answer_item.get('answer'))

    @classmethod
    def filter_result_answer(cls, **filters) -> List[ResultAnswer]:
        """
            Getting a list of result answer
        """
        return cls.model.objects.filter(**filters)
