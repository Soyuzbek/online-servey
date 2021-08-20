from django import forms
from django.contrib import admin

from worksheets.models import *


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_start', 'date_finish', 'created_at', 'updated_at')
    list_display_links = ('title', 'date_start', 'date_finish', 'created_at', 'updated_at')
    fields = ('title', 'description', 'date_start', 'date_finish', 'created_at', 'updated_at')
    list_filter = ('title', 'date_start', 'date_finish', 'created_at', 'updated_at')
    search_fields = ('title', 'date_start', 'date_finish', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('date_start',)
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_module_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False


class AnswerAdminForm(forms.ModelForm):
    def clean(self):
        is_right = self.cleaned_data['is_right']
        is_answer_text = self.cleaned_data['is_answer_text']
        answer_text = self.cleaned_data['answer_text']
        if is_right and is_answer_text:
            raise forms.ValidationError(
                {'is_answer_text': 'Вы должны выбрать только одно! Либо правильный ответ, либо ответ текстом.'})
        elif not is_right and is_answer_text and answer_text:
            raise forms.ValidationError({'is_answer_text': 'Вы выбрали ответ текстом. Удалите свой ответ!'})


class AnswerInline(admin.StackedInline):
    model = Answer
    form = AnswerAdminForm
    fields = ('answer_text', 'is_right', 'is_answer_text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    extra = 0

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_module_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'question_text', 'created_at', 'updated_at')
    list_display_links = ('quiz', 'question_text', 'created_at', 'updated_at')
    fields = ('quiz', 'question_text', 'created_at', 'updated_at')
    list_filter = ('quiz', 'question_text', 'created_at', 'updated_at')
    search_fields = ('quiz__title', 'question_text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('quiz',)
    inlines = (AnswerInline,)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_module_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False


class ResultAnswerInline(admin.StackedInline):
    model = ResultAnswer
    fields = ('answer', 'self_answer_text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    extra = 0

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_module_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'quiz', 'created_at', 'updated_at')
    list_display_links = ('first_name', 'second_name', 'quiz', 'created_at', 'updated_at')
    fields = ('first_name', 'second_name', 'quiz', 'created_at', 'updated_at')
    list_filter = ('first_name', 'second_name', 'quiz', 'created_at', 'updated_at')
    search_fields = ('first_name', 'second_name', 'quiz__title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('quiz',)
    inlines = (ResultAnswerInline,)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_module_permission(self, request):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False
