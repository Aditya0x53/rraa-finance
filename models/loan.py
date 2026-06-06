from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Loan:
    dlno: str
    customer_id: int
    principal_amount: float
    interest_rate: float
    interest_amount: float
    total_amount: float
    weekly_installment: float
    start_date: datetime
    expected_end_date: datetime
    balance: float
    status: str = "ACTIVE"
    scheduled_weeks: int = 10
    total_paid: float = 0.0
    remarks: Optional[str] = None
    loan_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "dlno": self.dlno,
            "customer_id": self.customer_id,
            "principal_amount": self.principal_amount,
            "interest_rate": self.interest_rate,
            "interest_amount": self.interest_amount,
            "total_amount": self.total_amount,
            "weekly_installment": self.weekly_installment,
            "scheduled_weeks": self.scheduled_weeks,
            "start_date": self.start_date,
            "expected_end_date": self.expected_end_date,
            "total_paid": self.total_paid,
            "balance": self.balance,
            "status": self.status,
            "remarks": self.remarks,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            loan_id=data.get("loan_id"),
            dlno=data.get("dlno"),
            customer_id=data.get("customer_id"),
            principal_amount=data.get("principal_amount"),
            interest_rate=data.get("interest_rate"),
            interest_amount=data.get("interest_amount"),
            total_amount=data.get("total_amount"),
            weekly_installment=data.get("weekly_installment"),
            scheduled_weeks=data.get("scheduled_weeks", 10),
            start_date=data.get("start_date"),
            expected_end_date=data.get("expected_end_date"),
            total_paid=data.get("total_paid", 0.0),
            balance=data.get("balance"),
            status=data.get("status", "ACTIVE"),
            remarks=data.get("remarks"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )