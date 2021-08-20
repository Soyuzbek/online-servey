from datetime import datetime

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.schemas.worksheets import QuizListSchema, QuestionListSchema, ResultListSchema, ResultDetailSchema
from common.utils import get_instance_slice
from worksheets.apis import *
from worksheets.services import *


class QuizListAPIView(APIView):
    permission_classes = (AllowAny,)
    schema = QuizListSchema()

    def get(self, request, *args, **kwargs):
        """
            Retrieving a list of quizzes
        """
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = QuizService.filter_quiz().order_by('-date_finish')[instance_slice]
        serializer = QuizListSerializer(queryset, many=True)
        return Response(data={
            'message': 'List of all quizzes',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)


class QuizDetailAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
            Getting a quiz
        """
        instance = QuizService.get_quiz(id=kwargs.get('pk'))
        serializer = QuizDetailSerializer(instance, many=False)
        return Response(data={
            'message': 'Quiz has been successfully found',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)


class QuestionListAPIView(APIView):
    permission_classes = (AllowAny,)
    schema = QuestionListSchema()

    def get(self, request, *args, **kwargs):
        """
            Retrieving a list of questions
        """
        quiz_id = int(request.query_params.get('quiz', '1'))
        queryset = QuestionService.filter_question(quiz_id=quiz_id)
        serializer = QuestionListSerializer(queryset, many=True)
        return Response(data={
            'message': 'List of all questions',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)


class ResultListAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    schema = ResultListSchema()

    def get(self, request, *args, **kwargs):
        """
            Retrieving a list of results
            headers - Authorization Token <token key>
        """
        queryset = ResultService.filter_result(user=request.user)
        serializer = ResultListSerializer(queryset, many=True)
        return Response(data={
            'message': 'List of all results',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
            Creation result
            headers - Authorization Token <token key>
        """
        serializer = ResultCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ResultService.create_result(
            hide=serializer.validated_data.get('hide_name'),
            f_name=serializer.validated_data.get('first_name'),
            s_name=serializer.validated_data.get('second_name'),
            quiz=serializer.validated_data.get('quiz'),
            answers=serializer.validated_data.get('result_answer'),
            user=request.user)
        return Response(data={
            'message': 'The result has been successfully created',
            'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)


class ResultDetailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    schema = ResultDetailSchema()

    def get(self, request, *args, **kwargs):
        """
            Getting a result
            headers - Authorization Token <token key>
        """
        instance = ResultService.get_result(pk=kwargs.get('pk'),
                                            user=request.user)
        serializer = ResultDetailSerializer(instance, many=False)
        return Response(data={
            'message': 'Result has been successfully found',
            'data': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)
