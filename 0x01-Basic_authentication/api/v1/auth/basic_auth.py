#!/usr/bin/env python3
"""
A class BasicAuth that inherits from Auth
"""

from .auth import Auth
import base64


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
