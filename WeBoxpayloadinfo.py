import random
import string
from datetime import datetime, timedelta

import globalvariables as globalvar
import globalvariables as info

sharedfolderslist = []
policyfolderslist = []

now_datetime = datetime.now()
start_of_day_datetime = now_datetime.replace(hour=00, minute=00, second=00)
end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59)
start_timestamp = int(round(start_of_day_datetime.timestamp() * 1000))
end_timestamp = int(round(end_of_day_datetime.timestamp() * 1000))
isostart = datetime.utcfromtimestamp(start_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
isoend = datetime.utcfromtimestamp(end_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.999Z')

# Get today's date
presentday = datetime.today()

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

C = 6
createglobalfolders = {
    "name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=C)),
    "policies": [],
    "shared": True,
    "actCode": globalvar.activationCode
}

B = 6
createpolicyfolders = {
    "name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=B)),
    "policies": [
        {
            "policyId": globalvar.Android_profile_ids,
            "policyName": globalvar.Android_profile_name,
            "policyType": globalvar.Android_profile_type
        }
    ],
    "shared": False,
    "actCode": globalvar.activationCode
}

PolicygroupconfigwithSign = {
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    },
    "signEnabled": True,
    "uploadSizeLimit": "10000000",
    "type": globalvar.Android_profile_type,
    "policyId": globalvar.Android_profile_ids
}

PolicygroupconfigwithoutSign = {
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    },
    "signEnabled": False,
    "uploadSizeLimit": "10000000",
    "type": globalvar.Android_profile_type,
    "policyId": globalvar.Android_profile_ids
}

SharedFolderconfigwithSign = {
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    },
    "signEnabled": True,
    "uploadSizeLimit": "5000000",
    "type": "Shared",
    "activationCode": globalvar.activationCode
}

SharedFolderconfigwithoutSign = {
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    },
    "signEnabled": False,
    "uploadSizeLimit": "5000000",
    "type": "Shared",
    "activationCode": globalvar.activationCode
}

AddingAmazonS3folder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 853,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": "120000",
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}

AddingDropboxfolder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 853,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "1586751147798907997",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/sh/9sirqndavlbv4lv/AACz95VSaVso9A_weDup3cwVa?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 9,
                "label": "QA Team"
            },
            {
                "uniqueID": "5014251260363229112",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/df49s38nvtjmnog/managing_securing_mobile_devices_9781119349846.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 9,
                "label": "MDM"
            },
            {
                "label": "WeBox",
                "fPath": "https://www.dropbox.com/s/tywjhg1lvluo8vl/WeBox.pdf?dl=0",
                "fileType": 9
            }
        ]
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}

AddingGoogleDrivefolder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 853,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "6950513484462702748",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/presentation/d/1qsL11PZssXMzXChY1vDiUfUjVtMsPkSHt1EZgZEU6OE/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "WeTalk Ppt"
            },
            {
                "uniqueID": "4530299940357623519",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/spreadsheets/d/1IffEvQGbnkj6pUqafyxl34I_cjuU-2sMrBandV1glfM/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "Daily API Testing Reports"
            },
            {
                "uniqueID": "2010684754122457284",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/17-KZMt4m4-RHUhzkZZWpcPyUejf09I-V/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "OD"
            },
            {
                "uniqueID": "7814880563540938678",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/15EZ5qO6GTvU7hPIdT9ZWDIRTg9Jh4QTV/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "SVG"
            }
        ]
    },
    "dropBox": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "8670003847332056822",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/tywjhg1lvluo8vl/WeBox.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "WeBox"
            },
            {
                "uniqueID": "1586751147798907997",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/sh/9sirqndavlbv4lv/AACz95VSaVso9A_weDup3cwVa?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "QA Team"
            },
            {
                "uniqueID": "5014251260363229112",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/df49s38nvtjmnog/managing_securing_mobile_devices_9781119349846.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "MDM"
            }
        ]
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}
AddingSDCardFolder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 852,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": "120000",
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "557035397307059925",
                "fName": None,
                "fSize": 0,
                "fPath": "Documents/Webox.pdf",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 6,
                "label": "QA"
            },
            {
                "label": "Testing ",
                "fPath": "Documents/WeGuard.pdf",
                "fileType": 6
            }
        ]
    },
    "googleDrive": {
        "enabled": False,
        "files": [
            {
                "uniqueID": "3518706255667481656",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/spreadsheets/d/1ivr53lYwNzWpeaxJ8sUMc4qNADGMtOuYGkuu2_dGSbA/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "Work Profile Report"
            },
            {
                "uniqueID": "6950513484462702748",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/presentation/d/1qsL11PZssXMzXChY1vDiUfUjVtMsPkSHt1EZgZEU6OE/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "WeTalk Ppt"
            },
            {
                "uniqueID": "4530299940357623519",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/spreadsheets/d/1IffEvQGbnkj6pUqafyxl34I_cjuU-2sMrBandV1glfM/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "Daily API Testing Reports"
            },
            {
                "uniqueID": "2010684754122457284",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/17-KZMt4m4-RHUhzkZZWpcPyUejf09I-V/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "OD"
            },
            {
                "uniqueID": "7814880563540938678",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/15EZ5qO6GTvU7hPIdT9ZWDIRTg9Jh4QTV/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "SVG"
            }
        ]
    },
    "dropBox": {
        "enabled": False,
        "files": [
            {
                "uniqueID": "8670003847332056822",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/tywjhg1lvluo8vl/WeBox.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "WeBox"
            },
            {
                "uniqueID": "1586751147798907997",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/sh/9sirqndavlbv4lv/AACz95VSaVso9A_weDup3cwVa?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "QA Team"
            },
            {
                "uniqueID": "5014251260363229112",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/df49s38nvtjmnog/managing_securing_mobile_devices_9781119349846.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "MDM"
            }
        ]
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}
configwithoutsignpolicygroupfolders = {
    "policyId": globalvar.Android_profile_ids,
    "s3Config": {
        "enabled": True,
        "identityPoolId": "",
        "region": "",
        "bucketName": []
    },
    "signEnabled": False,
    "uploadSizeLimit": "5000000"
}
configwithsignpolicygroupfolders = {
    "policyId": globalvar.Android_profile_ids,
    "s3Config": {
        "enabled": True,
        "identityPoolId": "",
        "region": "",
        "bucketName": []
    },
    "signEnabled": True,
    "uploadSizeLimit": "5000000"
}
DeletingDropboxFolder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 865,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": "120000",
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "8116472784163521206",
                "fName": None,
                "fSize": 0,
                "fPath": "Documents/WeGuard.pdf",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "6",
                "label": "Testing "
            }
        ]
    },
    "googleDrive": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "6950513484462702748",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/presentation/d/1qsL11PZssXMzXChY1vDiUfUjVtMsPkSHt1EZgZEU6OE/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "WeTalk Ppt"
            },
            {
                "uniqueID": "4530299940357623519",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/spreadsheets/d/1IffEvQGbnkj6pUqafyxl34I_cjuU-2sMrBandV1glfM/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "Daily API Testing Reports"
            },
            {
                "uniqueID": "2010684754122457284",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/17-KZMt4m4-RHUhzkZZWpcPyUejf09I-V/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "OD"
            },
            {
                "uniqueID": "7814880563540938678",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/15EZ5qO6GTvU7hPIdT9ZWDIRTg9Jh4QTV/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "SVG"
            }
        ]
    },
    "dropBox": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "5014251260363229112",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/df49s38nvtjmnog/managing_securing_mobile_devices_9781119349846.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 9,
                "label": "MDM"
            },
            {
                "uniqueID": "7761166636710774629",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/tywjhg1lvluo8vl/WeBox.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 9,
                "label": "WeBox"
            }
        ]
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}
DeletingGoogleDriveFolder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 865,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "8116472784163521206",
                "fName": None,
                "fSize": 0,
                "fPath": "Documents/WeGuard.pdf",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "6",
                "label": "Testing "
            }
        ]
    },
    "googleDrive": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "6950513484462702748",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/presentation/d/1qsL11PZssXMzXChY1vDiUfUjVtMsPkSHt1EZgZEU6OE/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "WeTalk Ppt"
            },
            {
                "uniqueID": "4530299940357623519",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/spreadsheets/d/1IffEvQGbnkj6pUqafyxl34I_cjuU-2sMrBandV1glfM/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "Daily API Testing Reports"
            },
            {
                "uniqueID": "2010684754122457284",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/17-KZMt4m4-RHUhzkZZWpcPyUejf09I-V/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 7,
                "label": "OD"
            }
        ]
    },
    "dropBox": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "5014251260363229112",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/df49s38nvtjmnog/managing_securing_mobile_devices_9781119349846.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "MDM"
            },
            {
                "uniqueID": "7761166636710774629",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/tywjhg1lvluo8vl/WeBox.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "WeBox"
            }
        ]
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}
DeletingSDCardFolder = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 853,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": [
            {
                "uniqueID": "8116472784163521206",
                "fName": None,
                "fSize": 0,
                "fPath": "Documents/WeGuard.pdf",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": 6,
                "label": "Testing "
            }
        ]
    },
    "googleDrive": {
        "enabled": False,
        "files": [
            {
                "uniqueID": "6950513484462702748",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/presentation/d/1qsL11PZssXMzXChY1vDiUfUjVtMsPkSHt1EZgZEU6OE/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "WeTalk Ppt"
            },
            {
                "uniqueID": "4530299940357623519",
                "fName": None,
                "fSize": 0,
                "fPath": "https://docs.google.com/spreadsheets/d/1IffEvQGbnkj6pUqafyxl34I_cjuU-2sMrBandV1glfM/edit?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "Daily API Testing Reports"
            },
            {
                "uniqueID": "2010684754122457284",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/17-KZMt4m4-RHUhzkZZWpcPyUejf09I-V/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "OD"
            },
            {
                "uniqueID": "7814880563540938678",
                "fName": None,
                "fSize": 0,
                "fPath": "https://drive.google.com/file/d/15EZ5qO6GTvU7hPIdT9ZWDIRTg9Jh4QTV/view?usp=sharing",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "7",
                "label": "SVG"
            }
        ]
    },
    "dropBox": {
        "enabled": False,
        "files": [
            {
                "uniqueID": "1586751147798907997",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/sh/9sirqndavlbv4lv/AACz95VSaVso9A_weDup3cwVa?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "QA Team"
            },
            {
                "uniqueID": "5014251260363229112",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/df49s38nvtjmnog/managing_securing_mobile_devices_9781119349846.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "MDM"
            },
            {
                "uniqueID": "7761166636710774629",
                "fName": None,
                "fSize": 0,
                "fPath": "https://www.dropbox.com/s/tywjhg1lvluo8vl/WeBox.pdf?dl=0",
                "fCheckSum": None,
                "fExtension": None,
                "timestamp": 0,
                "fileType": "9",
                "label": "WeBox"
            }
        ]
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": "us-west-2:9e8b7389-6218-4d4c-bca4-1768f3791613",
        "region": "us-west-2",
        "bucketName": [
            "laf-dev"
        ]
    }
}
disabledallowdownload = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 310,
    "allowDownload": False,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
disabledallowfileview = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": False,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
DisabledGoogleDriveDropbox = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 853,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": False,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
disabledopenwith = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": False,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
DisabledSDcardAmazonS3 = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 853,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
disabledservicetypes = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
disabledshowlinks = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
disabledweboxpasscode = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": True,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledallowdownload = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": False,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": False,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledfileview = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": False,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledopenwith = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": False,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledAmzazonS3SDcard = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledservicetypes = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledshowlinks = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledweboxpasscode = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": "123456",
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": True,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": True,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}
enabledgoogledrivedropbox = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 13,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": True,
    "allowFileView": True,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": True,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": True,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": True,
        "files": None
    },
    "dropBox": {
        "enabled": True,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}

noWeBoxConfigs = {
    "id": "64cc93d57fa1a20102b8de2e",
    "deleted": False,
    "version": 310,
    "policyId": globalvar.Android_profile_ids,
    "allowDownload": False,
    "allowFileView": False,
    "allowDownloadOnlyOnWiFi": False,
    "allowDownloadOnNetwork": False,
    "allowDownloadOnNWWiFI": True,
    "openWith": False,
    "passcode": None,
    "passcodeInterval": 120000,
    "showLinks": False,
    "sdCard": {
        "enabled": False,
        "files": None
    },
    "googleDrive": {
        "enabled": False,
        "files": None
    },
    "dropBox": {
        "enabled": False,
        "files": None
    },
    "s3Config": {
        "enabled": False,
        "identityPoolId": None,
        "region": None,
        "bucketName": None
    }
}

undosave = {
    "topic": "webox" + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
    "type": "FILES_UPDATE",
    "message": "WeBox msg",
    "isLicenseLevel": True,
    "actCode": globalvar.activationCode,
    "pActCode": globalvar.productActivationCode
}

WeBoxFiles = {"id": "602f542efce9661c0f83bb5b", "deleted": False, "createdBy": info.userName,
              "createdAt": "2021-02-19T06:01:18.609+0000", "updatedBy": info.userName,
              "updatedAt": "2021-04-01T11:31:26.961+0000", "version": 52, "policyId": globalvar.Android_profile_ids,
              "allowDownload": True, "allowFileView": True, "allowDownloadOnlyOnWiFi": False,
              "allowDownloadOnNetwork": False, "allowDownloadOnNWWiFI": True, "openWith": True,
              "passcode": None, "passcodeInterval": 120000, "showLinks": True,
              "sdCard": {"enabled": True, "files": None},
              "googleDrive": {"enabled": True, "files": None}, "dropBox": {"enabled": True, "files": None},
              "s3Config": {"enabled": True, "identityPoolId": None, "region": None, "bucketName": None}}

pdf = [{"uploadId": None, "imageFileName": "WeBox_Img_1614175174747.jpg",
        "imageFileURL": "https://laf-dev.s3.us-west-2.amazonaws.com/0NTFI/CTRC-AA5WU/WeBox_Img_1614175174747.jpg",
        "imageLabel": "WeBox_Img_1614175174747",
        "signatureURL": "https://laf-dev.s3.us-west-2.amazonaws.com/0NTFI/CTRC-AA5WU/Sign_1614175183899.jpg",
        "signatureFileName": "Sign_1614175183899.jpg", "timestamp": "2021-02-24T14:30:04.0950Z",
        "imageFileCheckSum": "32beb1deaaa3deb8f49da133bcc72544",
        "signatureFileCheckSum": "b659e40396ddd79fa2704e2b40ae34f0", "deviceId": "869881036785080",
        "policyId": globalvar.Android_profile_ids, "filePath": "Chakrapani AE/WeBox_Img_1614175174747.jpg",
        "folderName": "Chakrapani AE", "sharedFolder": True, "imageFileSize": 2859824, "singnatureFileSize": 20588,
        "comment": "", "imageCreatedTime": 1614175184126},
       {"uploadId": None, "imageFileName": "WeBox_Img_1614175226974.jpg",
        "imageFileURL": "https://laf-dev.s3.us-west-2.amazonaws.com/0NTFI/CTRC-AA5WU/WeBox_Img_1614175226974.jpg",
        "imageLabel": "WeBox_Img_1614175226974",
        "signatureURL": "https://laf-dev.s3.us-west-2.amazonaws.com/0NTFI/CTRC-AA5WU/Sign_1614175240505.jpg",
        "signatureFileName": "Sign_1614175240505.jpg", "timestamp": "2021-02-24T14:30:54.0590Z",
        "imageFileCheckSum": "280a3c8312cf718cbe26444ae99dfd9f",
        "signatureFileCheckSum": "0dafd603b130a96adaa99ed348c62d89", "deviceId": "869881036785080",
        "policyId": globalvar.Android_profile_ids, "filePath": "Chakrapani AE/WeBox_Img_1614175226974.jpg",
        "folderName": "Chakrapani AE", "sharedFolder": True, "imageFileSize": 3423576, "singnatureFileSize": 27844,
        "comment": " Captured", "imageCreatedTime": 1614175240762},
       {"uploadId": None, "imageFileName": "WeBox_Img_1615467544017.jpg",
        "imageFileURL": "https://qa-cache.weguard.io/0NTFI/CTRC-AA5WU/mobile/=fO=G3PLCTc6wJMu2PPb2xvYHDEYduGE8n3y1NmTXQ2RT9LO9i2i7xFbINSkpLc8/WeBox_Img_1615467544017.jpg",
        "imageLabel": "WeBox_Img_1615467544017",
        "signatureURL": "https://qa-cache.weguard.io/0NTFI/CTRC-AA5WU/mobile/y9QaLGeuAFk6jpaSsBQ=nn9zA7MFyna1JQDHADVGEaiV4MF_dZVZkbt8OGqOTgRe/Sign_1615467549059.jpg",
        "signatureFileName": "Sign_1615467549059.jpg", "timestamp": "2021-03-11T13:29:16.0670Z",
        "imageFileCheckSum": "6546898b83b995018fb9094c33a657b0",
        "signatureFileCheckSum": "3cd27fb96f7309459affc19826f95627", "deviceId": "860362040109798",
        "policyId": globalvar.Android_profile_ids, "filePath": "Chakrapani AE/WeBox_Img_1615467544017.jpg",
        "folderName": "Chakrapani AE", "sharedFolder": True, "imageFileSize": 2543834, "singnatureFileSize": 0,
        "comment": "", "imageCreatedTime": 1615467549331}]
zip = [
    "https://qa-cache.weguard.io/0NTFI/CTRC-AA5WU/mobile/sYTjdJu7r65DFH4sfZ_56U9fwFUux7ubYvPebp=bTuK=qDAtyfhU8u7qdiSz--G6/WeBox_Img_1615457010085.jpg"]
