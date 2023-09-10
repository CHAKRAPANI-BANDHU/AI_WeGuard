import os
import time
from datetime import datetime, timedelta
import WeGuardLogger as WeGuard

# Environment Variables
global userName
userName = ''
global password
password = ''
global BaseURL
BaseURL = ''
global loglevel
loglevel = 0

# Pagination
page_1 = 1
page_100 = 100
page_500 = 500
page_1000 = 1000
page_50000 = 50000

if os.environ.get('WEGUARD_USER') is not None:
    userName = os.getenv('WEGUARD_USER')

if os.environ.get('WEGUARD_PASS') is not None:
    password = os.getenv('WEGUARD_PASS')

if os.environ.get('QA_BASEURL') is not None:
    BaseURL = os.getenv('QA_BASEURL')

if os.environ.get('LOG_LEVEL') is not None:
    loglevel = int(os.environ['LOG_LEVEL'])

log_file = "WeGuard_" + time.strftime("%d-%m-%Y_%H%M%S") + ".log"
#log_level = 2  # Change this to set the desired log level (0 to 4)
WeGuard.configure_logger(log_file, loglevel)

timeout = 600
bearerToken = ""
activationCode = ""
productActivationCode = ""
fname = ""
lname = ""
accountId = ""
companyName = ""
name = ""
enterpriseId = ""


UnacknowledgeAlertsIDs = []

# Policy Groups Information of Android, iOS and Windows from common policy
# After clicking on policy groups on left navigation bar
# Android Policies Info
Android_profiles = []
Android_profile_ids = []
Android_profile_name = []
Android_profile_type = []
Android_profile_platform = []

# Android Devices Info
Android_Mongo_DB_DeviceIDs = []
Android_Devices = []
Android_DeviceIDs = []

# Windows Policies Info
Windows_profiles = []
Windows_profile_ids = []
Windows_profile_name = []
Windows_profile_type = []
Windows_profile_platform = []

# Windows Devices Info
Windows_Mongo_DB_DeviceIDs = []
Windows_Devices = []
Windows_DeviceIDs = []

# iOS Policies Info
iOS_profiles = []
iOS_profile_ids = []
iOS_profile_name = []
iOS_profile_type = []
iOS_profile_platform = []

# iOS Devices Info
iOS_Mongo_DB_DeviceIDs = []
iOS_Devices = []
iOS_DeviceIDs = []

# disable apps ids from get api
disableapps_list = []


# Geofence Information
GEOFENCE_IDS=[]
GEOFENCE_MONGO_DB_IDS=[]
GEOFENCE_TYPES=[]

# Time Conversion in different formats
now_datetime = datetime.now()
start_of_day_datetime = now_datetime.replace(hour=00, minute=00, second=00)
end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59)
start_timestamp = int(round(start_of_day_datetime.timestamp() * 1000))
end_timestamp = int(round(end_of_day_datetime.timestamp() * 1000))
isostart = datetime.utcfromtimestamp(start_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
isoend = datetime.utcfromtimestamp(end_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.999Z')

# Get today's date
presentday = datetime.today()
presentday_timestamp = int(presentday.timestamp() * 1000)

# Calculate the start of yesterday
yesterday_start = (presentday - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
yesterday_start_timestamp = int(yesterday_start.timestamp() * 1000)
isoyesterday_start_timestamp = datetime.utcfromtimestamp(yesterday_start_timestamp / 1000).strftime(
    '%Y-%m-%dT%H:%M:%S.000Z')

# Calculate the end of yesterday
yesterday_end = (presentday - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=999999)
yesterday_end_timestamp = int(yesterday_end.timestamp() * 1000)
isoyesterday_end_timestamp = datetime.utcfromtimestamp(yesterday_end_timestamp / 1000).strftime(
    '%Y-%m-%dT%H:%M:%S.000Z')

# Get Yesterday
yesterday = presentday.replace(hour=23, minute=59, second=59) - timedelta(1)
yesterday_timestamp = int(round(yesterday.timestamp() * 1000))
isoyesterday = datetime.utcfromtimestamp(yesterday_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
# Get custom date
custom = presentday.replace(hour=23, minute=59, second=59) - timedelta(2)
custom_timestamp = int(round(custom.timestamp() * 1000))
isocustom = datetime.utcfromtimestamp(custom_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')

# Get custom 1 week date
C1week = presentday.replace(hour=23, minute=59, second=59) - timedelta(4)
custom_1week_timestamp = int(round(C1week.timestamp() * 1000))
iso1weekcustom = datetime.utcfromtimestamp(custom_1week_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')

# Get Tomorrow
tomorrow = presentday + timedelta(1)
customnextdate = presentday.replace(hour=23, minute=59, second=59) + timedelta(2)
customnextdate_timestamp = int(round(customnextdate.timestamp() * 1000))

# Get month
month = presentday.replace(hour=23, minute=59, second=59) - timedelta(30)
month_timestamp = int(round(month.timestamp() * 1000))
isomonth = datetime.utcfromtimestamp(month_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')

# Calculate the start of the current month
start_of_month = presentday.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

# Calculate the end of the previous month
end_of_previous_month = start_of_month - timedelta(seconds=1)

# Calculate the start of the previous month
start_of_previous_month = end_of_previous_month.replace(day=1)

# Convert timestamps to milliseconds
start_of_previous_month_timestamp = int(start_of_previous_month.timestamp() * 1000)
end_of_previous_month_timestamp = int(end_of_previous_month.timestamp() * 1000)
start_of_month = presentday.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
start_of_month_timestamp = int(start_of_month.timestamp() * 1000)
end_of_month = start_of_month.replace(day=presentday.day, hour=0, minute=0, second=0, microsecond=0)
end_of_month_timestamp = int(start_of_month.timestamp() * 1000)
end_of_previous_month = start_of_month - timedelta(seconds=1)
start_of_previous_month = end_of_previous_month.replace(day=1)
