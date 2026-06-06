import logging
from datetime import datetime
from config import DATABASE_PATH

logger = logging.getLogger(__name__)


def run_migrations(db):
    """Run database migrations"""
    try:
        migration_version = get_migration_version(db)
        
        if migration_version < 1:
            migration_001_initial_schema(db)
        
        logger.info("All migrations completed successfully")
    except Exception as e:
        logger.error(f"Migration failed: {str(e)}")
        raise


def get_migration_version(db):
    """Get current migration version"""
    try:
        result = db.fetchone("SELECT setting_value FROM settings WHERE setting_name = 'migration_version'")
        if result:
            return int(result[0])
        return 0
    except:
        return 0


def set_migration_version(db, version):
    """Set migration version"""
    db.execute(
        "INSERT OR REPLACE INTO settings (setting_name, setting_value) VALUES (?, ?)",
        ("migration_version", str(version))
    )


def migration_001_initial_schema(db):
    """Migration 001: Initial schema setup"""
    try:
        logger.info("Running migration 001: Initial schema setup")
        set_migration_version(db, 1)
        logger.info("Migration 001 completed")
    except Exception as e:
        logger.error(f"Migration 001 failed: {str(e)}")
        raise