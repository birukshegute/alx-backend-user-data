#!/usr/bin/env python3
"""Handle user sessions in database"""
from models.base import Base


class UserSession(Base):
    """Class for handling user sessions."""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize the class."""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
