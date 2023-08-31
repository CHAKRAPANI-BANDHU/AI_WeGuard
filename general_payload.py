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

PostPolicyLevelAlertConfig = {"accountId": globalvariables.accountId, "policyId": globalvariables.Android_profile_ids,
                              "batteryWarningEmailList": None, "batteryLowEmailList": None,
                              "batteryCriticalEmailList": None, "dataUsageWarningEmailList": None,
                              "dataUsageLowEmailList": None, "dataUsageCriticalEmailList": None,
                              "kioskLockedEmailList": None, "kioskUnLockedEmailList": None,
                              "adminLockedEmailList": None, "deviceRebootedEmailList": None,
                              "deviceWipedEmailList": None, "deviceDeletedEmailList": None, "deviceLostEmailList": None,
                              "deviceStolenEmailList": None, "deviceReplacedEmailList": None,
                              "deviceConnectedBackEmailList": None, "memoryWarningEmailList": None,
                              "memoryLowEmailList": None, "memoryCriticalEmailList": None,
                              "discUsageWarningEmailList": None, "discUsageLowEmailList": None,
                              "discUsageCriticalEmailList": None, "simRemovedEmailList": None,
                              "simChangedEmailList": None, "simAddedEmailList": None, "simLockedEmailList": None,
                              "resetPasswordEmailList": None}

# PUT Alerts Config
fake = Faker()  # Generate a random Gmail address
Notifications = {
    "accountId": globalvariables.accountId,
    "policyId": None,
    "batteryWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "batteryLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "batteryCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "dataUsageWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "dataUsageLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "dataUsageCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "kioskLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "kioskUnLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "adminLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceRebootedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceWipedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceDeletedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceLostEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceStolenEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceReplacedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceConnectedBackEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "memoryWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "memoryLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "memoryCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "discUsageWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "discUsageLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "discUsageCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simRemovedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simChangedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simAddedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "resetPasswordEmailList": [
        fake.email()  # Generate a random Gmail address
    ]
}

# Notification Microservice -- POST Alerts Config
PostAccountLevelAlertConfig = {"accountId": globalvariables.accountId, "policyId": None,
                               "batteryWarningEmailList": None, "batteryLowEmailList": None,
                               "batteryCriticalEmailList": None, "dataUsageWarningEmailList": None,
                               "dataUsageLowEmailList": None, "dataUsageCriticalEmailList": None,
                               "kioskLockedEmailList": None, "kioskUnLockedEmailList": None,
                               "adminLockedEmailList": None, "deviceRebootedEmailList": None,
                               "deviceWipedEmailList": None, "deviceDeletedEmailList": None,
                               "deviceLostEmailList": None, "deviceStolenEmailList": None,
                               "deviceReplacedEmailList": None, "deviceConnectedBackEmailList": None,
                               "memoryWarningEmailList": None, "memoryLowEmailList": None,
                               "memoryCriticalEmailList": None, "discUsageWarningEmailList": None,
                               "discUsageLowEmailList": None, "discUsageCriticalEmailList": None,
                               "simRemovedEmailList": None, "simChangedEmailList": None, "simAddedEmailList": None,
                               "simLockedEmailList": None, "resetPasswordEmailList": None}

# PUT Alerts Config
fake = Faker()  # Generate a random Gmail address
PutAccountLevelNotifications = {
    "accountId": globalvariables.accountId,
    "policyId": None,
    "batteryWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "batteryLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "batteryCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "dataUsageWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "dataUsageLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "dataUsageCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "kioskLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "kioskUnLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "adminLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceRebootedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceWipedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceDeletedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceLostEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceStolenEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceReplacedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "deviceConnectedBackEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "memoryWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "memoryLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "memoryCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "discUsageWarningEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "discUsageLowEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "discUsageCriticalEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simRemovedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simChangedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simAddedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "simLockedEmailList": [
        fake.email()  # Generate a random Gmail address
    ],
    "resetPasswordEmailList": [
        fake.email()  # Generate a random Gmail address
    ]
}