import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def create_schema(db):
    """Create all database tables"""
    try:
        # Customers table
        db.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                address TEXT,
                id_proof TEXT,
                guarantor TEXT,
                photo_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Loans table
        db.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                dlno TEXT NOT NULL UNIQUE,
                customer_id INTEGER NOT NULL,
                principal_amount REAL NOT NULL,
                interest_rate REAL DEFAULT 25,
                interest_amount REAL NOT NULL,
                total_amount REAL NOT NULL,
                weekly_installment REAL NOT NULL,
                scheduled_weeks INTEGER DEFAULT 10,
                start_date TIMESTAMP NOT NULL,
                expected_end_date TIMESTAMP NOT NULL,
                total_paid REAL DEFAULT 0,
                balance REAL NOT NULL,
                status TEXT DEFAULT 'ACTIVE',
                remarks TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)

        # Collections table
        db.execute("""
            CREATE TABLE IF NOT EXISTS collections (
                collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER NOT NULL,
                customer_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                installment_equivalent REAL,
                collection_date TIMESTAMP NOT NULL,
                remarks TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (loan_id) REFERENCES loans(loan_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)

        # Penalties table
        db.execute("""
            CREATE TABLE IF NOT EXISTS penalties (
                penalty_id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER NOT NULL,
                penalty_amount REAL NOT NULL,
                reason TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
            )
        """)

        # Users table
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Audit logs table
        db.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT NOT NULL,
                entity_type TEXT,
                entity_id INTEGER,
                details TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        # Settings table
        db.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
                setting_name TEXT NOT NULL UNIQUE,
                setting_value TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create indexes
        db.execute("CREATE INDEX IF NOT EXISTS idx_customer_phone ON customers(phone)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_loan_dlno ON loans(dlno)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_loan_customer ON loans(customer_id)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_loan_status ON loans(status)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_collection_loan ON collections(loan_id)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_collection_date ON collections(collection_date)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_logs(timestamp)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_user_username ON users(username)")

        logger.info("Database schema created successfully")
        return True

    except Exception as e:
        logger.error(f"Schema creation failed: {str(e)}")
        raise