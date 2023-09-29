import random
import string

from faker import Faker

import globalvariables

fake = Faker()
# Generate a random Gmail email address
random_gmail_address = fake.email(domain="gmail.com")

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
    "policyIdList": globalvariables.Android_Policy_IDs
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
    "policyIdList": globalvariables.Android_Policy_IDs
}

DisableAllDevicesState = {
    "search": None,
    "provisioned": False,
    "replaced": False,
    "lost": False,
    "stolen": False,
    "unEnrolled": False,
    "active": False,
    "policyIdList": globalvariables.Android_Policy_IDs
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

# Company Directory
# Random ID Eight Digits
RandomContactsIDs = random.randint(10000000, 99999999)
FCMUpdateAfterAddingContacts_PolicyLevel = {
    "topic": globalvariables.activationCode + "_" + globalvariables.productActivationCode, "type": "SYNC_CONTACTS",
    "isLicenseLevel": True,
    "actCode": globalvariables.activationCode,
    "pActCode": globalvariables.productActivationCode, "message": None, "id": RandomContactsIDs}


# Create contacts at Account Level
# Define a function to generate a random Gmail address
def random_email_address(length=10):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return f"{username}@gmail.com"


name = string.ascii_letters + string.digits
randomName = ''.join(random.choice(name) for _ in range(10))

# Generate a random Gmail address
random_email = random_email_address()

# Define a list of possible values for each field
address_types = ["Home", "Work", "Other"]
streets = ["Attapur", "Johnson", "Bidar"]
countries = ["India", "USA", "India"]
cities = ["Hyderabad", "Texas", "Bidar"]
states = ["Telangana", "Alabama", "Karnataka"]
zipcodes = ["500048", "67894450", "585401"]

# Generate a random postal address
postal_address = {
    "addressType": random.choice(address_types),
    "street": random.choice(streets),
    "country": random.choice(countries),
    "city": random.choice(cities),
    "state": random.choice(states),
    "zipcode": random.choice(zipcodes)
}
# Create the payload with the random email address
firstName = ''.join(random.choice(string.ascii_letters) for _ in range(10))
lastName = ''.join(random.choice(string.ascii_letters) for _ in range(10))
displayName = ''.join(random.choice(string.ascii_letters) for _ in range(10))
nickName = ''.join(random.choice(string.ascii_letters) for _ in range(6))
companyName = ''.join(random.choice(string.ascii_letters) for _ in range(10))
jobTitle = ''.join(random.choice(string.ascii_letters) for _ in range(10))
website = "https://www." + ''.join(random.choice(string.ascii_letters) for _ in range(10)) + ".com"
notes = ''.join(random.choice(string.ascii_letters) for _ in range(10))
emailAddresses = [{"emailType": "Home", "emailAddress": random_email_address()}]
phoneNums = [{"phone": [''.join(random.choice(string.digits) for _ in range(10))]}]
postalAddresses = [postal_address]

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
                               "uninstallWeguardEmailList": [random_gmail_address]}

# Appending it from loop in the code
PostPolicyLevelAlertConfig = {"accountId": None, "policyId": None,
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
                              "uninstallWeguardEmailList": [random_gmail_address]}

# Geofence Information
GeofenceIDS = []
Geofence_MongoDB_IDs = []
GeofenceTypes = []
# Generate and store random Geofence IDs
GeofenceIds = [str(random.randint(1000000000000000000, 9999999999999999999)) for _ in range(1)]  # Generate 1 random IDs

# Delete Geofence Notifications
# Generate a random boolean value for 'enabled' field
enabled_values = random.choice([True, False])
# Generate a random geofenceType value
geofenceType_values = random.choice(["IN_FENCE", "OUT_FENCE"])
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
geofence_id_list = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(geofence_id_length)) for
                    _ in range(geofence_id_length)]
# Create an empty payload dictionary
DeleteGeofenceNotificationsPayload = {
    "emailList": [random_gmail_address],
    "enabled": enabled_values,
    "geofenceId": random_geofence_id,
    "geofenceIdList": geofence_id_list,
    "geofenceType": geofenceType_values,
    "id": random_id,
    "policyId": random_policy_id
}

# Windows Microservices
PUT_UpdateTags_Windows_Device = {"tag1": "In-House -- Chakrapani",
                                 "tag4": None,
                                 "tag3": "QA"}

# Generate a random 4-digit number room ID for WeSupport
random_number = random.randint(1000, 9999)
# Format it as a string with double colons
Room_ID = f"::{random_number}"
RandomID = RandomContactsIDs

# Session IDs
random_number = random.randint(100000000, 999999999)
SessionID = random_number

# Initialize the test_data list
Allowed_Actions = {}
Supported_Values = []
