import os
from pathlib import Path
from datetime import datetime

# Application Configuration
APP_NAME = "RRAA Finance"
APP_VERSION = "1.0.0"
APP_AUTHOR = "RRAA Finance Team"

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
REPORTS_DIR = BASE_DIR / "reports"
DATABASE_DIR = BASE_DIR / "database"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)

# Database Configuration
DATABASE_PATH = DATABASE_DIR / "rraa_finance.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Finance Rules
FIXED_INTEREST_RATE = 0.25  # 25%
SCHEDULED_WEEKS = 10
CURRENCY = "₹"

# UI Configuration
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"

# Theme Colors
THEME_COLORS = {
    "primary": "#0a1428",      # Dark Navy
    "secondary": "#ffc107",    # Gold
    "success": "#28a745",      # Green
    "danger": "#dc3545",       # Red
    "warning": "#ffc107",      # Yellow/Gold
    "info": "#17a2b8",         # Cyan
    "light": "#f8f9fa",        # Light Gray
    "dark": "#0a1428",         # Dark Navy
}

# Role Configuration
ROLES = {
    "admin": "Administrator",
    "manager": "Manager",
    "operator": "Operator"
}

# Pagination
ITEMS_PER_PAGE = 20

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# File Upload
MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "pdf"}

# Report Generation
REPORT_FORMATS = ["PDF", "Excel", "CSV"]

# Date Format
DATE_FORMAT = "%d-%m-%Y"
DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"
TIME_FORMAT = "%H:%M:%S"

# Feature Flags
ENABLE_PENALTIES = True
ENABLE_AUDIT_LOG = True
ENABLE_AUTO_BACKUP = True
ENABLE_THERMAL_PRINTER = False

# Backup Configuration
AUTO_BACKUP_INTERVAL = 3600  # seconds (1 hour)
BACKUP_RETENTION_DAYS = 30