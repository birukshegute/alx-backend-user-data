#!/usr/bin/env python3
"""
A class BasicAuth that inherits from Auth
"""

from .auth import Auth
import base64
from models.user import User
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
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and Retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        b64_auth_header = \
            self.extract_base64_authorization_header(auth_header)
        if b64_auth_header is None:
            return None
        decoded_auth_header = \
            self.decode_base64_authorization_header(b64_auth_header)
        if decoded_auth_header is None:
            return None
        user_email, user_pwd = \
            self.extract_user_credentials(decoded_auth_header)
        if user_email is None or user_pwd is None:
            return None
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
