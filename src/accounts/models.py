from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from accounts.managers import BaseUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(blank=False, null=False, unique=True, verbose_name=_('почтовый адрес'))
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('пароль'))
    is_superuser = models.BooleanField(default=False, blank=True, verbose_name=_('администратор'))
    is_staff = models.BooleanField(default=False, blank=True, verbose_name=_('сотрудник'))
    is_active = models.BooleanField(default=False, blank=True, verbose_name=_('активный'))

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'usr'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        ordering = ('created_at',)


