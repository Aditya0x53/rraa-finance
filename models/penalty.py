from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Penalty:
    loan_id: int
    penalty_amount: float
    reason: Optional[str] = None
    penalty_id: Optional[int] = None
    created_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "penalty_id": self.penalty_id,
            "loan_id": self.loan_id,
            "penalty_amount": self.penalty_amount,
            "reason": self.reason,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            penalty_id=data.get("penalty_id"),
            loan_id=data.get("loan_id"),
            penalty_amount=data.get("penalty_amount"),
            reason=data.get("reason"),
            created_at=data.get("created_at"),
        )