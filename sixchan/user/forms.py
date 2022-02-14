from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from sixchan.config import (
    DISPLAY_NAME_MAX_LENGTH,
    PASSWORD_REGEX,
    USERNAME_MAX_LENGTH,
    USERNAME_REGEX,
)


class ChangeUsernameForm(FlaskForm):
    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired(),
            Regexp(USERNAME_REGEX),
            Length(max=USERNAME_MAX_LENGTH),
        ],
    )


class ChangeEmailForm(FlaskForm):
    new_email = StringField(
        "新しいメールアドレス",
        validators=[DataRequired(), Email()],
    )


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(
        "現在のパスワード",
        validators=[
            DataRequired(),
            Regexp(PASSWORD_REGEX),
        ],
    )
    new_password = PasswordField(
        "新しいパスワード",
        validators=[
            DataRequired(),
            Regexp(PASSWORD_REGEX),
            EqualTo("new_password_confirmation"),
        ],
    )
    new_password_confirmation = PasswordField(
        "新しいパスワード(確認)",
        validators=[DataRequired(), Regexp(PASSWORD_REGEX)],
    )


class ProfileForm(FlaskForm):
    display_name = StringField(
        "表示名",
        validators=[Length(max=DISPLAY_NAME_MAX_LENGTH)],
    )
    introduction = TextAreaField(
        "自己紹介",
        validators=[Length(max=DISPLAY_NAME_MAX_LENGTH)],
    )