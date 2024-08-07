#!/usr/bin/env python3
"""
A class BasicAuth that inherits from Auth
"""

from .auth import Auth


class BasicAuth(Auth):
    """A class that inherits from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if not authorization_header:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]
