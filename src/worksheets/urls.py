from django.urls import path
from worksheets import views

urlpatterns = [
    path('quizzes/<int:pk>', views.QuizDetailAPIView.as_view(), name='get-quizzes'),
    path('quizzes', views.QuizListAPIView.as_view(), name='list-quizzes'),
    path('questions', views.QuestionListAPIView.as_view(), name='list-questions'),
    path('results/<int:pk>', views.ResultDetailAPIView.as_view(), name='get-result'),
    path('results', views.ResultListAPIView.as_view(), name='create-result')
]
