#!/usr/bin/env python3
"""
A class BasicAuth that inherits from Auth
"""

from .auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """A class that inherits from Auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if not authorization_header:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of base64_authorization_header:"""
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            decoded = base64.b64decode(
                    base64_authorization_header,
                    validate=True)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns user email and password from the Base64 decoded value"""
        if not decoded_base64_authorization_header:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password"""
        if not user_email or type(user_email) != str:
            return None
        if not user_pwd or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
        return None
