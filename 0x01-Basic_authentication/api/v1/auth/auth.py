#!/usr/bin/env python3
"""
Manages the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False - path and excluded_paths that will be used later"""
        return False

    def authorization_header(self, request=None) -> str:
        """that returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None"""
        return None
