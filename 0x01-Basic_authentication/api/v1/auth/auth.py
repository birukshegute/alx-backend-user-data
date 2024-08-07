#!/usr/bin/env python3
"""
Manages the API authentication.
"""

from flask import request
import fnmatch
from typing import List, TypeVar


class Auth:
    """ Class to manage manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if path isn't in the list of strings excluded_paths"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """that returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None"""
        return None
