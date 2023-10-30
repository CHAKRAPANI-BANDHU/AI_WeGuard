import random
import string
import uuid

from faker import Faker

import globalvariables

fake = Faker()
# Generate a random Gmail email address
random_gmail_address = fake.email(domain="gmail.com")

# Define the base DeviceState with all keys set to None
Base_DeviceState = {
    "search": None,
    "provisioned": None,
    "replaced": None,
    "lost": None,
    "stolen": None,
    "unEnrolled": None,
    "active": None,
    "policyIdList": None
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

FilterByGroupName = {
    "search": None,
    "provisioned": True,
    "replaced": False,
    "lost": False,
    "stolen": False,
    "unEnrolled": False,
    "active": False,
    "policyIdList": globalvariables.AllPlatformPolicyIDs
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

# Generate a random UUID
my_uuid = uuid.uuid4()
# Format the UUID to match the specified format
UUID = '-'.join([my_uuid.hex[:8], my_uuid.hex[8:12], my_uuid.hex[12:16], my_uuid.hex[16:20], my_uuid.hex[20:]])

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
geofencePolicyConfigId = []
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

# Broadcast Message and Title
# Lists of sample titles and messages
titles = ["Important Update", "Breaking News", "Weather Forecast", "Daily Quote", "Tech Tips"]
messages = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Don't forget to stay hydrated today!",
    "Python is a versatile programming language.",
    "Today's weather: sunny with a chance of rain.",
    "Life is 10% what happens to us and 90% how we react to it.",
]
# Generate random titles and messages
random_title = random.choice(titles)
random_message = random.choice(messages)

# Windows Policy Update (PUT) payload

WindowsPolicyUpdate= {
  "id": globalvariables.PolicyWindowsID,
  "deleted": False,
  "version": globalvariables.PolicyWindowsVersion,
  "runGenericCSPAutoFlag": False,
  "runGenericCSPAutoFreq": 24,
  "accountId": "64cb86dd80f4b80b1dc65e73",
  "name": "ThinkPad Users",
  "type": "WINDOWS",
  "description": "Default Windows Policy",
  "deviceCount": 0,
  "general": {
    "allowWifi": 1,
    "allowAutoConnectToWiFiSenseHotspots": 1,
    "allowInternetSharing": 1,
    "allowBluetooth": 2,
    "allowUSBConnection": 1,
    "allowCamera": 1,
    "hideShutDown": 0,
    "hidePowerButton": 0,
    "letAppsAccessLocation": 1,
    "allowWifiToggle": False,
    "allowInternetSharingToggle": False,
    "allowBluetoothToggle": False,
    "allowUSBConnectionToggle": False,
    "allowCameraToggle": False,
    "hideShutDownToggle": False,
    "hidePowerButtonToggle": False,
    "letAppsAccessLocationToggle": False,
    "allowEndTask": None
  },
  "network": {
    "allowManualWiFiConfiguration": 1,
    "wlanScanMode": 100,
    "wifiConfigurationList": None,
    "allowManualWiFiConfigurationToggle": True
  },
  "branding": {
    "desktopImageUrl": "Min: , Max: ",
    "lockScreenImageUrl": "Min: , Max: "
  },
  "applications": [
    {
      "type": "APPX",
      "appExtension": None,
      "appName": "SampleApp_1.0.1",
      "packageFamilyName": "SampleApp.WeGuard_b819snfg442cg",
      "packageIdentityName": None,
      "publisherCertificateName": None,
      "windowsPhoneLegacyId": None,
      "productId": "",
      "upgradeCode": None,
      "version": "1.0.1.0",
      "hash": "5AFB41617C68A45283ADD60C885560FDF343A9E845C3E9D9073F36265F7D2E03",
      "appUrl": "https://stage-cache.weguard.ai/qa-cache-weguard-io/windows-apps/64cb86dd80f4b80b1dc65e73/5AFB41617C68A45283ADD60C885560FDF343A9E845C3E9D9073F36265F7D2E03/SampleApp_1.0.1.appx",
      "icon": None,
      "commandLine": None,
      "timeout": None,
      "retryCount": None,
      "retryInterval": None,
      "certificateId": "64d5d84428d37d4342513366"
    },
    {
      "type": "MSI",
      "appExtension": None,
      "appName": "putty-0.76-installer",
      "packageFamilyName": "",
      "packageIdentityName": None,
      "publisherCertificateName": None,
      "windowsPhoneLegacyId": None,
      "productId": "8CFE5E4E-970A-4380-A782-AF6E609574F1",
      "upgradeCode": None,
      "version": "0.76.0.0",
      "hash": "381A5390E362528DC1028DAD04C849EF640D4B53A31E801874467DC716A43864",
      "appUrl": "https://stage-cache.weguard.ai/qa-cache-weguard-io/windows-apps/64cb86dd80f4b80b1dc65e73/381A5390E362528DC1028DAD04C849EF640D4B53A31E801874467DC716A43864/putty-0.76-installer.msi",
      "icon": None,
      "commandLine": "/quiet",
      "timeout": 5,
      "retryCount": 3,
      "retryInterval": 5,
      "certificateId": None
    },
    {
      "type": "MSI",
      "appExtension": None,
      "appName": "FileZilla FTP Client",
      "packageFamilyName": "",
      "packageIdentityName": None,
      "publisherCertificateName": None,
      "windowsPhoneLegacyId": None,
      "productId": "DE37B7E5-4245-4635-AFC8-595E86CC3760",
      "upgradeCode": None,
      "version": "3.50.0.0",
      "hash": "38C4DF43C955827D0D131B0FDA8F455564B53E3C0D7127DA62AAD6ED01D2D688",
      "appUrl": "https://stage-cache.weguard.ai/qa-cache-weguard-io/windows-apps/64cb86dd80f4b80b1dc65e73/38C4DF43C955827D0D131B0FDA8F455564B53E3C0D7127DA62AAD6ED01D2D688/FileZillaFTPClient.msi",
      "icon": None,
      "commandLine": "/quiet",
      "timeout": 5,
      "retryCount": 3,
      "retryInterval": 5,
      "certificateId": None
    },
    {
      "type": "MSI",
      "appExtension": None,
      "appName": "Password Generator",
      "packageFamilyName": "",
      "packageIdentityName": None,
      "publisherCertificateName": None,
      "windowsPhoneLegacyId": None,
      "productId": "386CB99A-7F52-4DA7-82B5-FBF5D7F1FD80",
      "upgradeCode": None,
      "version": "1.1.0",
      "hash": "0F2A874FAE28813C0BB65A776B62F4216249B8AB9ABA3FD98D6D0B7B4AE814B2",
      "appUrl": "https://stage-cache.weguard.ai/qa-cache-weguard-io/windows-apps/64cb86dd80f4b80b1dc65e73/0F2A874FAE28813C0BB65A776B62F4216249B8AB9ABA3FD98D6D0B7B4AE814B2/PasswordGenerator.msi",
      "icon": None,
      "commandLine": "/quiet",
      "timeout": 5,
      "retryCount": 3,
      "retryInterval": 5,
      "certificateId": None
    }
  ],
  "security": {
    "configAutomaticRestartSignOn": 0,
    "allowAutomaticRestartSignOn": 1,
    "launchAppAfterLogOn": None,
    "allowEndTask": 1,
    "allowManualUnenrollment": 1,
    "allowStorageCard": 1,
    "threat": {
      "securityThreatEnable": 1,
      "antiExploit": 1,
      "behavioralScan": 1,
      "antivirus": 1,
      "filescan": 1
    },
    "virusconfig": {
      "enableVirusScan": 1,
      "frequency": "Weekly",
      "time": 66060000,
      "scheduledDate": 1698172200000,
      "weekDay": "Wednesday"
    },
    "syncFrequency": 0,
    "queueFrequency": 0,
    "tLaunchAppAfterLogOn": []
  },
  "bitlocker": None,
  "vpnConfiguration": None,
  "certificates": None,
  "systemUpdate": {
    "allowAutoUpdate": 2,
    "activeHoursStart": 8,
    "activeHoursEnd": 17,
    "allowUpdateService": 1,
    "allowMUUpdateService": 1,
    "allowNonMicrosoftSignedUpdate": 0,
    "scheduledInstallDay": 0,
    "scheduledInstallEveryWeek": 0,
    "scheduledInstallFirstWeek": 0,
    "scheduledInstallFourthWeek": 0,
    "scheduledInstallSecondWeek": 0,
    "scheduledInstallThirdWeek": 0,
    "scheduledInstallTime": 3,
    "excludeWUDriversInQualityUpdate": 0,
    "updateServiceUrl": None,
    "updateServiceUrlAlternate": None,
    "deferFeatureUpdatesPeriodInDays": 0,
    "pauseFeatureUpdates": 0,
    "pauseFeatureUpdatesStartTime": None,
    "deferQualityUpdatesPeriodInDays": 0,
    "configureDeadlineForFeatureUpdates": 7,
    "configureDeadlineForQualityUpdates": 7,
    "configureDeadlineGracePeriod": 2,
    "configureDeadlineNoAutoReboot": 0,
    "configureFeatureUpdateUninstallPeriod": 10
  },
  "secureBrowser": {
    "edge": {
      "urlAllowList": None,
      "urlBlockList": None,
      "defaultCookiesSetting": 1,
      "blockExternalExtensions": 1,
      "proxySettings": {
        "proxyBypassList": None,
        "proxyMode": None,
        "proxyPacUrl": None,
        "proxyServer": None
      }
    },
    "chrome": None
  },
  "deviceLock": {
    "devicePasswordEnabled": 1,
    "allowSimpleDevicePassword": 0,
    "alphanumericDevicePasswordRequired": 2,
    "devicePasswordExpiration": 0,
    "devicePasswordHistory": 0,
    "minDevicePasswordLength": 4,
    "minDevicePasswordComplexCharacters": 4,
    "maxDevicePasswordFailedAttempts": 0,
    "minimumPasswordAge": 0,
    "maxInactivityTimeDeviceLock": 0
  },
  "proApplications": [
    {
      "type": "MSI",
      "appExtension": None,
      "appName": "WeGuard",
      "packageFamilyName": None,
      "packageIdentityName": None,
      "publisherCertificateName": None,
      "windowsPhoneLegacyId": None,
      "productId": "7C7A241D-FA5A-429B-A5BF-2E42A9535F9D",
      "upgradeCode": "501690EE-A067-4A20-AEB7-86573D4A27C6",
      "version": "4.9.0.0",
      "hash": "1C479592E6EFCB90F01056B7CFC4E8A731E6AB2DB392C358035674C0B17FA54F",
      "appUrl": "https://stage-cache.weguard.ai/qa-cache-weguard-io/windows-apps/weguard/1C479592E6EFCB90F01056B7CFC4E8A731E6AB2DB392C358035674C0B17FA54F/WeGuardSetup_4.9.0.0.msi",
      "icon": None,
      "commandLine": "BASE_URL=https://qa-api-gw.weguard.ai/windows",
      "timeout": 5,
      "retryCount": 10,
      "retryInterval": 5,
      "certificateId": None
    }
  ],
  "trackConfig": {
    "enable": True,
    "syncFrequencyInSec": 60,
    "backupSyncFrequencyInSec": 1800,
    "coapLocationUrl": None
  },
  "usageEventsConfig": {
    "sendBoot": True,
    "sendShutdown": True,
    "sendSuspend": True,
    "sendResume": True,
    "sendLogin": True,
    "sendLogoff": True,
    "sendLock": True,
    "sendUnlock": True,
    "sendScreenTime": True
  },
  "generalCsp": None,
  "clonedFrom": "64def314bd707e7c59640015",
  "clonedFromName": "VIRT Users",
  "licenseRefreshTime": 0,
  "geofences": None,
  "policyEmail": "e2zg589065324b872f973c346dc22136@weguard.com",
  "retryTime": 1697805860138,
  "weGuardEnabled": True,
  "weShieldEnabled": True,
  "weSupportEnabled": True,
  "weGuardRmmEnabled": True,
  "healthCheckEnabled": True,
  "appRetryCount": 10,
  "appRetryInterval": 5,
  "systemApps": None,
  "enableKiosk": False,
  "enableSingleAppKiosk": False
}