import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class QuizListSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='page', required=False, location='query',
                              schema=coreschema.String(description='int (default=0)')),
                coreapi.Field(name='count', required=False, location='query',
                              schema=coreschema.String(description='int (default=9)')),
            ]
        return self._manual_fields + api_fields


class QuestionListSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='quiz', required=True, location='query',
                              schema=coreschema.String(description='int')),
            ]
        return self._manual_fields + api_fields


class ResultListSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'POST':
            api_fields = [
                coreapi.Field(name='hide_name', required=True, location='form',
                              schema=coreschema.String(description='bool')),
                coreapi.Field(name='first_name', required=True, location='form',
                              schema=coreschema.String(description='str')),
                coreapi.Field(name='second_name', required=True, location='form',
                              schema=coreschema.String(description='str')),
                coreapi.Field(name='quiz', required=True, location='form',
                              schema=coreschema.String(description='id (quiz object)')),
                coreapi.Field(name='result_answer', required=True, location='form',
                              schema=coreschema.String(description='result_answer: [{"answer": id (answer object),'
                                                                   '                 "self_answer_text": str}]')),
            ]
        elif method == 'GET':
            return self._manual_fields
        return self._manual_fields + api_fields


class ResultDetailSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        api_fields = []
        if method == 'GET':
            api_fields = [
                coreapi.Field(name='id', required=True, location='form',
                              schema=coreschema.String(description='int')),
            ]
        return self._manual_fields + api_fields