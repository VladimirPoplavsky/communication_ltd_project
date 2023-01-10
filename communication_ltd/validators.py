import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from . import configReadingHelper

config = configReadingHelper.read_config()

passwordLength = int(config['Password Management']['Password Length'])
# allowUpperCase = config['Password Management']['Allow Upper-case Letters in Password (y/n)']
# allowLowerCase = config['Password Management']['Allow Lower-case Letters in Password (y/n)']
# allowNumbers = config['Password Management']['Allow numbers in Password (y/n)']
# allowSpecialCharacters = config['Password Management']['Allow Special Characters in Password (y/n)']
passwordComplexity = config['Password Management']['Password Complexity']
passwordHistory = config['Password Management']['Password History']
passwordBlackList = config['Password Management']['Password Black List']
maxTryToLogin = int(config['Password Management']['Max Try to Login'])


class PasswordComplexityValidator(object):
    def validate(self, password, user=None):
        if re.search("upperCase", passwordComplexity):
            if not re.findall('[A-Z]', password):
                raise ValidationError(
                    _("The password must contain at least 1 uppercase letter, A-Z."),
                    code='password_no_upper',
                )

        if re.search("lowerCase", passwordComplexity):
            if not re.findall('[a-z]', password):
                raise ValidationError(
                    _("The password must contain at least 1 lowercase letter, a-z."),
                    code='password_no_lower',
                )

        if re.search("numbers", passwordComplexity):
            if not re.findall('\d', password):
                raise ValidationError(
                    _("The password must contain at least 1 digit, 0-9."),
                    code='password_no_number',
                )

        if re.search("specialCharacters", passwordComplexity):
            if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
                raise ValidationError(
                    _("The password must contain at least 1 symbol: " +
                      "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                    code='password_no_symbol',
                )

    def get_help_text(self):
        return _(
            "Your password must meet complexity requirements:"
        )


class PasswordBlacklistValidator(object):
    def validate(self, password, user=None):
        if re.search(password, passwordBlackList):
            raise ValidationError(
                _("You may not use that password"),
                code='blacklist password',
            )

    def get_help_text(self):
        return _(
            "You may not use that password"
        )
