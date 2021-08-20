from typing import Tuple, List

from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework.authtoken.models import Token

from accounts.models import User
from common.exceptions import ObjectNotFoundException, ObjectAlreadyExistException
from common.validators import validate_user_password


class TokenService:
    model = Token

    @classmethod
    def create_auth_token(cls, email: str, password: str) -> Tuple[User, Token, Token]:
        """
            Creating a token for a user
        """
        user = authenticate(username=email, password=password)
        if user:
            token, created = cls.model.objects.get_or_create(user=user)
            return user, token, created
        else:
            raise ObjectNotFoundException('User not found or not active')

    @classmethod
    def destroy_auth_token(cls, user: User) -> None:
        """
            Removing a token for a user
        """
        return cls.model.objects.filter(user=user).delete()


class UserService:
    model = User

    @classmethod
    def get_user(cls, **filters) -> User:
        """
            Getting one user
        """
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('User not found')

    @classmethod
    def create_user(cls, email: str, password: str, conf_password: str, **kwargs) -> User:
        """
            User creation
        """
        if cls.filter_user(email=email).exists():
            raise ObjectAlreadyExistException('User with this email already exists')
        user = cls.model(email=email, **kwargs)
        correct_password = validate_user_password(password=password, conf_password=conf_password)
        user.set_password(correct_password)
        user.save()
        return user

    @classmethod
    def filter_user(cls, **filters) -> List[User]:
        """
            Getting a list of users
        """
        return cls.model.objects.filter(**filters)

    @classmethod
    def exclude_user(cls, **filters) -> List[User]:
        """
            Exclude a user from the list
        """
        return cls.model.objects.exclude(**filters)