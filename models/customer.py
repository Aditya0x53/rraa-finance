from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Customer:
    name: str
    phone: str
    address: Optional[str] = None
    id_proof: Optional[str] = None
    guarantor: Optional[str] = None
    photo_path: Optional[str] = None
    customer_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "address": self.address,
            "id_proof": self.id_proof,
            "guarantor": self.guarantor,
            "photo_path": self.photo_path,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            customer_id=data.get("customer_id"),
            name=data.get("name"),
            phone=data.get("phone"),
            address=data.get("address"),
            id_proof=data.get("id_proof"),
            guarantor=data.get("guarantor"),
            photo_path=data.get("photo_path"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )