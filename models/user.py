from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    username: str
    password_hash: str
    role: str
    user_id: Optional[int] = None
    is_active: bool = True
    created_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role,
            "is_active": self.is_active,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get("user_id"),
            username=data.get("username"),
            password_hash=data.get("password_hash"),
            role=data.get("role"),
            is_active=data.get("is_active", True),
            created_at=data.get("created_at"),
        )