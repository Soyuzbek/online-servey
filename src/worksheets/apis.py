from rest_framework import serializers
from worksheets.models import *


class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'date_start', 'date_finish')


class QuizDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'date_start', 'date_finish', 'created_at', 'updated_at')


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text', 'is_right', 'is_answer_text')


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text', 'is_right', 'is_answer_text')


class ResultAnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultAnswer
        fields = ('self_answer_text',)


class QuestionDetailSerializer(serializers.ModelSerializer):
    answer = AnswerDetailSerializer(many=True)
    questions = ResultAnswerDetailSerializer(many=False)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'answer', 'questions')


class QuestionListSerializer(serializers.ModelSerializer):
    answer = AnswerListSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'answer')


class QuizNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'date_start', 'date_finish')


class ResultAnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultAnswer
        fields = ('answer', 'self_answer_text',)


class ResultAnswerDetailSerializer(serializers.ModelSerializer):
    answer = AnswerDetailSerializer(many=False)

    class Meta:
        model = ResultAnswer
        fields = ('answer', 'self_answer_text',)


class ResultCreateSerializer(serializers.ModelSerializer):
    result_answer = ResultAnswerCreateSerializer(many=True)

    class Meta:
        model = Result
        fields = ('hide_name', 'first_name', 'second_name', 'quiz', 'result_answer')


class ResultListSerializer(serializers.ModelSerializer):
    quiz = QuizListSerializer(many=False)

    class Meta:
        model = Result
        fields = ('id', 'quiz',)


class ResultDetailSerializer(serializers.ModelSerializer):
    quiz = QuizNestedSerializer(many=False)
    results_answer = ResultAnswerDetailSerializer(many=True)

    class Meta:
        model = Result
        fields = ('hide_name', 'first_name', 'second_name', 'quiz', 'results_answer')
