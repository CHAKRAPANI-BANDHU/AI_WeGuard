import random
import string

from faker import Faker

import globalvariables

login_event = {
    "agent": "PORTAL",
    "actorId": globalvariables.userName,
    "policyId": None,
    "type": "",
    "msg": "",
    "action": "-",
    "event": "Enterprise",
    "sentTime": globalvariables.start_timestamp,
    "sourceIP": "",
    "logLevel": "Info",
    "log": "Logged in",
    "activationCode": globalvariables.activationCode,
    "productActivationCode": globalvariables.productActivationCode,
    "metadata": "{}"
}

AllDevices = {
    "search": None,
    "provisioned": True,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "active": None,
    "policyIdList": None
}

AndroidPoliciesDevices = {
    "search": None,
    "provisioned": True,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "active": None,
    "policyIdList": globalvariables.Android_profile_ids
}

UnenrolledDevices = {
    "search": None,
    "provisioned": None,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": True,
    "active": None,
    "policyIdList": None
}

LostDevices = {
    "search": None,
    "provisioned": None,
    "replaced": None,
    "lost": True,
    "stolen": None,
    "unEnrolled": True,
    "active": None,
    "policyIdList": None
}

StolenDevices = {
    "search": None,
    "provisioned": None,
    "replaced": None,
    "lost": None,
    "stolen": True,
    "unEnrolled": None,
    "active": None,
    "policyIdList": None
}

ActiveDevices = {
    "search": None,
    "provisioned": None,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "active": True,
    "policyIdList": None
}

ReplacedDevices = {
    "search": None,
    "provisioned": None,
    "replaced": True,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "active": True,
    "policyIdList": None
}

EnableAllDevicesState = {
    "search": None,
    "provisioned": True,
    "replaced": True,
    "lost": True,
    "stolen": True,
    "unEnrolled": True,
    "active": True,
    "policyIdList": globalvariables.Android_profile_ids
}

DisableAllDevicesState = {
    "search": None,
    "provisioned": False,
    "replaced": False,
    "lost": False,
    "stolen": False,
    "unEnrolled": False,
    "active": False,
    "policyIdList": globalvariables.Android_profile_ids
}

FilterByGroupName = {
    "search": None,
    "provisioned": False,
    "replaced": False,
    "lost": False,
    "stolen": False,
    "unEnrolled": False,
    "active": False,
    "policyIdList": None
}

AndroidDevices = {
    "search": None,
    "provisioned": True,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "type": "ANDROID",
    "active": None,
    "policyIdList": None
}

iOSDevices = {
    "search": None,
    "provisioned": True,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "type": "IOS",
    "active": None,
    "policyIdList": None
}

WindowsDevices = {
    "search": None,
    "provisioned": True,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "type": "WINDOWS",
    "active": None,
    "policyIdList": None
}

AllYesterdayLogs = {
  "startDate": globalvariables.yesterday_start_timestamp,
  "endDate": globalvariables.yesterday_end_timestamp,
  "event": "All",
  "logLevel": "All",
  "deviceIds": [],
  "policyIds": None
}

AllCustom1MonthLogs = {
  "startDate": globalvariables.start_of_month_timestamp,
  "endDate": globalvariables.presentday_timestamp,
  "event": "All",
  "logLevel": "All",
  "deviceIds": [],
  "policyIds": None
}

logout = {
    "agent": "PORTAL",
    "actorId": globalvariables.userName,
    "policyId": None,
    "type": "Info",
    "msg": "Logged out",
    "action": "-",
    "event": "Logout",
    "sentTime": globalvariables.start_timestamp,
    "sourceIP": ""
}

fake = Faker()

# Generate a random Gmail email address
random_gmail_address = fake.email(domain="gmail.com")

# PUT Alerts Config
fake = Faker()  # Generate a random Gmail address

# Notification Information
getAccountLevelNotificationId = []
getPolicyLevelNotificationId = []

AccountID = ""

# PUT Alerts Config
PutAccountLevelNotifications = {
    "accountId": None,
    "policyId": None,
    "batteryWarningEmailList": [random_gmail_address],
    "batteryLowEmailList": [random_gmail_address],
    "batteryCriticalEmailList": [random_gmail_address],
    "dataUsageWarningEmailList": [random_gmail_address],
    "dataUsageLowEmailList": [random_gmail_address],
    "dataUsageCriticalEmailList": [random_gmail_address],
    "kioskLockedEmailList": [random_gmail_address],
    "kioskUnLockedEmailList": [random_gmail_address],
    "adminLockedEmailList": [random_gmail_address],
    "deviceRebootedEmailList": [random_gmail_address],
    "deviceWipedEmailList": [random_gmail_address],
    "deviceDeletedEmailList": [random_gmail_address],
    "deviceLostEmailList": [random_gmail_address],
    "deviceStolenEmailList": [random_gmail_address],
    "deviceReplacedEmailList": [random_gmail_address],
    "deviceConnectedBackEmailList": [random_gmail_address],
    "memoryWarningEmailList": [random_gmail_address],
    "memoryLowEmailList": [random_gmail_address],
    "memoryCriticalEmailList": [random_gmail_address],
    "discUsageWarningEmailList": [random_gmail_address],
    "discUsageLowEmailList": [random_gmail_address],
    "discUsageCriticalEmailList": [random_gmail_address],
    "simRemovedEmailList": [random_gmail_address],
    "simChangedEmailList": [random_gmail_address],
    "simAddedEmailList": [random_gmail_address],
    "simLockedEmailList": [random_gmail_address],
    "resetPasswordEmailList": [random_gmail_address],
    "uninstallWeguardEmailList": [random_gmail_address]
}

PutPolicyLevelNotifications = {
    "accountId": None,
    "policyId": None,
    "batteryWarningEmailList": [random_gmail_address],
    "batteryLowEmailList": [random_gmail_address],
    "batteryCriticalEmailList": [random_gmail_address],
    "dataUsageWarningEmailList": [random_gmail_address],
    "dataUsageLowEmailList": [random_gmail_address],
    "dataUsageCriticalEmailList": [random_gmail_address],
    "kioskLockedEmailList": [random_gmail_address],
    "kioskUnLockedEmailList": [random_gmail_address],
    "adminLockedEmailList": [random_gmail_address],
    "deviceRebootedEmailList": [random_gmail_address],
    "deviceWipedEmailList": [random_gmail_address],
    "deviceDeletedEmailList": [random_gmail_address],
    "deviceLostEmailList": [random_gmail_address],
    "deviceStolenEmailList": [random_gmail_address],
    "deviceReplacedEmailList": [random_gmail_address],
    "deviceConnectedBackEmailList": [random_gmail_address],
    "memoryWarningEmailList": [random_gmail_address],
    "memoryLowEmailList": [random_gmail_address],
    "memoryCriticalEmailList": [random_gmail_address],
    "discUsageWarningEmailList": [random_gmail_address],
    "discUsageLowEmailList": [random_gmail_address],
    "discUsageCriticalEmailList": [random_gmail_address],
    "simRemovedEmailList": [random_gmail_address],
    "simChangedEmailList": [random_gmail_address],
    "simAddedEmailList": [random_gmail_address],
    "simLockedEmailList": [random_gmail_address],
    "resetPasswordEmailList": [random_gmail_address],
    "uninstallWeguardEmailList": [random_gmail_address]
}

# Notification Microservice -- POST Alerts Config
PostAccountLevelAlertConfig = {"accountId": None, "policyId": None,
                               "batteryWarningEmailList": [random_gmail_address], "batteryLowEmailList": [random_gmail_address],
                               "batteryCriticalEmailList": [random_gmail_address], "dataUsageWarningEmailList": [random_gmail_address],
                               "dataUsageLowEmailList": [random_gmail_address], "dataUsageCriticalEmailList": [random_gmail_address],
                               "kioskLockedEmailList": [random_gmail_address], "kioskUnLockedEmailList": [random_gmail_address],
                               "adminLockedEmailList": [random_gmail_address], "deviceRebootedEmailList": [random_gmail_address],
                               "deviceWipedEmailList": [random_gmail_address], "deviceDeletedEmailList": [random_gmail_address],
                               "deviceLostEmailList": [random_gmail_address], "deviceStolenEmailList": [random_gmail_address],
                               "deviceReplacedEmailList": [random_gmail_address], "deviceConnectedBackEmailList": [random_gmail_address],
                               "memoryWarningEmailList": [random_gmail_address], "memoryLowEmailList": [random_gmail_address],
                               "memoryCriticalEmailList": [random_gmail_address], "discUsageWarningEmailList": [random_gmail_address],
                               "discUsageLowEmailList": [random_gmail_address], "discUsageCriticalEmailList": [random_gmail_address],
                               "simRemovedEmailList": [random_gmail_address], "simChangedEmailList": [random_gmail_address], "simAddedEmailList": [random_gmail_address],
                               "simLockedEmailList": [random_gmail_address], "resetPasswordEmailList": [random_gmail_address],
                               "uninstallWeguardEmailList": [random_gmail_address]}

# Appending it from loop in the code
PostPolicyLevelAlertConfig = {"accountId": None, "policyId": None,
                               "batteryWarningEmailList": [random_gmail_address], "batteryLowEmailList": [random_gmail_address],
                               "batteryCriticalEmailList": [random_gmail_address], "dataUsageWarningEmailList": [random_gmail_address],
                               "dataUsageLowEmailList": [random_gmail_address], "dataUsageCriticalEmailList": [random_gmail_address],
                               "kioskLockedEmailList": [random_gmail_address], "kioskUnLockedEmailList": [random_gmail_address],
                               "adminLockedEmailList": [random_gmail_address], "deviceRebootedEmailList": [random_gmail_address],
                               "deviceWipedEmailList": [random_gmail_address], "deviceDeletedEmailList": [random_gmail_address],
                               "deviceLostEmailList": [random_gmail_address], "deviceStolenEmailList": [random_gmail_address],
                               "deviceReplacedEmailList": [random_gmail_address], "deviceConnectedBackEmailList": None,
                               "memoryWarningEmailList": [random_gmail_address], "memoryLowEmailList": [random_gmail_address],
                               "memoryCriticalEmailList": [random_gmail_address], "discUsageWarningEmailList": [random_gmail_address],
                               "discUsageLowEmailList": [random_gmail_address], "discUsageCriticalEmailList": [random_gmail_address],
                               "simRemovedEmailList": [random_gmail_address], "simChangedEmailList": [random_gmail_address], "simAddedEmailList": [random_gmail_address],
                               "simLockedEmailList": [random_gmail_address], "resetPasswordEmailList": [random_gmail_address],
                               "uninstallWeguardEmailList": [random_gmail_address]}

# Geofence Information
GeofenceIDS =[]
Geofence_MongoDB_IDs =[]
# Generate and store random Geofence IDs
GeofenceIds = [str(random.randint(1000000000000000000, 9999999999999999999)) for _ in range(5)]  # Generate 5 random IDs
GeofenceTypes =[]


# Delete Geofence Notifications
# Generate a random boolean value for 'enabled' field
enabled_value = random.choice([True, False])
# Generate a random geofenceType value
geofenceType_value = random.choice(["IN_FENCE", "OUT_FENCE"])
# Real values
real_policy_id = "64f5beb2d46ba149306f7a39"
real_id = "64f6f1febf131e7e65603568"
real_geofence_id = "1693906462740226730"
# Generate random values with the same length as the real values
random_policy_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(real_policy_id)))
random_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(real_id)))
random_geofence_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(real_geofence_id)))
geofence_id_length = 19
# Generate a list of random geofence IDs with the specified length
geofence_id_list = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(geofence_id_length)) for _ in range(geofence_id_length)]
# Create an empty payload dictionary
DeleteGeofenceNotificationsPayload = {
    "emailList": [random_gmail_address],
    "enabled": enabled_value,
    "geofenceId": random_geofence_id,
    "geofenceIdList": geofence_id_list,
    "geofenceType": geofenceType_value,
    "id": random_id,
    "policyId": random_policy_id
}

PUTGeofence = {
    "emailList": [random_gmail_address],
    "enabled": enabled_value
}