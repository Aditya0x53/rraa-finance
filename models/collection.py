from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Collection:
    loan_id: int
    customer_id: int
    amount: float
    collection_date: datetime
    installment_equivalent: Optional[float] = None
    remarks: Optional[str] = None
    collection_id: Optional[int] = None
    created_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "collection_id": self.collection_id,
            "loan_id": self.loan_id,
            "customer_id": self.customer_id,
            "amount": self.amount,
            "installment_equivalent": self.installment_equivalent,
            "collection_date": self.collection_date,
            "remarks": self.remarks,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            collection_id=data.get("collection_id"),
            loan_id=data.get("loan_id"),
            customer_id=data.get("customer_id"),
            amount=data.get("amount"),
            collection_date=data.get("collection_date"),
            installment_equivalent=data.get("installment_equivalent"),
            remarks=data.get("remarks"),
            created_at=data.get("created_at"),
        )