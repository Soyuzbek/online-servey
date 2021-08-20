from common.exceptions import IncorrectPasswordException
from secrets import compare_digest


def validate_user_password(password: str, conf_password: str) -> str:
    if not compare_digest(password, conf_password):
        raise IncorrectPasswordException('Passwords must match')
    return password
