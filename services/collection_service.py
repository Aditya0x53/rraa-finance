import logging
from typing import List, Optional
from datetime import datetime
from database import get_db_connection
from models import Collection
from .loan_service import LoanService

logger = logging.getLogger(__name__)


class CollectionService:
    def __init__(self):
        self.db = get_db_connection()
        self.loan_service = LoanService()

    def record_collection(self, collection: Collection) -> int:
        try:
            query = """
                INSERT INTO collections 
                (loan_id, customer_id, amount, installment_equivalent, collection_date, remarks)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor = self.db.execute(
                query,
                (collection.loan_id, collection.customer_id, collection.amount,
                 collection.installment_equivalent, collection.collection_date, collection.remarks)
            )
            
            loan = self.loan_service.get_loan(collection.loan_id)
            new_total_paid = loan.total_paid + collection.amount
            self.loan_service.update_loan_balance(collection.loan_id, new_total_paid)
            
            logger.info(f"Collection recorded for loan: {collection.loan_id}")
            return cursor.lastrowid
        except Exception as e:
            logger.error(f"Error recording collection: {str(e)}")
            raise

    def get_collection(self, collection_id: int) -> Optional[Collection]:
        try:
            query = "SELECT * FROM collections WHERE collection_id = ?"
            result = self.db.fetchone(query, (collection_id,))
            
            if result:
                return self._parse_collection(result)
            return None
        except Exception as e:
            logger.error(f"Error fetching collection: {str(e)}")
            raise

    def get_loan_collections(self, loan_id: int) -> List[Collection]:
        try:
            query = "SELECT * FROM collections WHERE loan_id = ? ORDER BY collection_date DESC"
            results = self.db.fetchall(query, (loan_id,))
            
            collections = []
            for result in results:
                collections.append(self._parse_collection(result))
            return collections
        except Exception as e:
            logger.error(f"Error fetching loan collections: {str(e)}")
            raise

    def get_customer_collections(self, customer_id: int) -> List[Collection]:
        try:
            query = "SELECT * FROM collections WHERE customer_id = ? ORDER BY collection_date DESC"
            results = self.db.fetchall(query, (customer_id,))
            
            collections = []
            for result in results:
                collections.append(self._parse_collection(result))
            return collections
        except Exception as e:
            logger.error(f"Error fetching customer collections: {str(e)}")
            raise

    def get_daily_collections(self, date: datetime) -> List[Collection]:
        try:
            query = """
                SELECT * FROM collections 
                WHERE DATE(collection_date) = DATE(?)
                ORDER BY collection_date DESC
            """
            results = self.db.fetchall(query, (date,))
            
            collections = []
            for result in results:
                collections.append(self._parse_collection(result))
            return collections
        except Exception as e:
            logger.error(f"Error fetching daily collections: {str(e)}")
            raise

    def get_daily_collection_total(self, date: datetime) -> float:
        try:
            query = """
                SELECT SUM(amount) FROM collections 
                WHERE DATE(collection_date) = DATE(?)
            """
            result = self.db.fetchone(query, (date,))
            return result[0] or 0.0
        except Exception as e:
            logger.error(f"Error calculating daily collection total: {str(e)}")
            raise

    def get_collection_statistics(self) -> dict:
        try:
            total_collections_result = self.db.fetchone("SELECT SUM(amount) FROM collections")
            total_records_result = self.db.fetchone("SELECT COUNT(*) FROM collections")
            
            return {
                "total_collected": total_collections_result[0] or 0.0,
                "total_records": total_records_result[0] or 0,
            }
        except Exception as e:
            logger.error(f"Error getting collection statistics: {str(e)}")
            raise

    def _parse_collection(self, result) -> Collection:
        return Collection(
            collection_id=result[0],
            loan_id=result[1],
            customer_id=result[2],
            amount=result[3],
            installment_equivalent=result[4],
            collection_date=result[5],
            remarks=result[6],
            created_at=result[7],
        )