import os, modules, datetime

# Directories
DATA_DIR = os.path.join(os.getcwd(), 'data')
REPORTS_DIR = os.path.join(DATA_DIR, 'reports')
LOGS_DIR = os.path.join(DATA_DIR, 'logs')
ERRORS_DIR = os.path.join(DATA_DIR, 'errors')

# Files
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
FILEPATH_LOG = os.path.join(LOGS_DIR, f'ghislieri_bot {datetime.datetime.now().strftime(DATETIME_FORMAT)}.log')

# Reporter
UPDATE_SECONDS_INTERVAL = 10