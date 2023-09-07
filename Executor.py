# If you turn this off, login will not be executed and subsequent test cases should be skipped.
must_run = 1

# Run only selected tests that I need to execute. Usually this should be normally set to 0
my_cases = 0

# Turn it to 1 for sanity tests only, 0 to execute other tests.
sanitytest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
regressiontest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
usualtest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
regression_tests = 0

negative_tests = 1
positive_tests = 1

# Run all positive cases
test_tc_0001_Login = 1
test_tc_0002_Login_Event = 1
test_tc_1000_Logout = 1

# Run all negative cases
test_tc_000003_AccountAdmin_Invalid_email = 1
test_tc_000004_AccountAdmin_Invalid_password = 1
test_tc_000005_AccountAdmin_Invalid_credentials = 1
test_tc_000006_AccountAdmin_Credentials_with_spaces = 1
test_tc_000007_AccountAdmin_Without_username = 1
test_tc_000008_AccountAdmin_Without_password = 1
test_tc_000009_AccountAdmin_Without_username_password = 1

# Devices Page
test_tc_00002_All_Devices_100 = 1
test_tc_00003_All_Devices_500 = 1
test_tc_00004_All_Devices_1000 = 1
test_tc_00005_Unenrolled_Devices = 1
test_tc_00006_Stolen_Devices = 1
test_tc_00007_Replaced_Devices = 1
test_tc_00008_Active_Devices = 1
test_tc_00009_Lost_Devices = 1
test_tc_00010_Unprovisioned_Devices = 1
test_tc_00011_Search_Policy = 1
test_tc_00012_Filter_By_GroupNames = 1
test_tc_00013_Enable_All_DevicesState = 1
test_tc_00014_Disable_All_DevicesState = 1
test_tc_00015_Android_Devices = 1
test_tc_00016_iOS_Devices = 1
test_tc_00017_Windows_Devices = 1

# Policy Groups
test_tc_0003_Policy_All = 1

# WeBox
test_tc_001_WeBox_AlLOWDownload = 1
test_tc_001_WeBox_licensepagesize = 1
test_tc_001_WeBox_FilesinAndroidPolicies = 1
test_tc_001_WeBox_FilesiniOSPolicies = 1
test_tc_001_WeBox_AndroidPolicy = 1
test_tc_001_WeBox_undosave = 1
test_tc_001_Webox_filespost = 1
test_tc_001_WeBox_Uploader = 1
test_tc_001_WeBox_AlLOWFileView = 1
test_tc_001_WeBox_OpenWith = 1
test_tc_001_WeBox_ShowLinks = 1
test_tc_001_noWeBoxConfigs = 1
test_tc_001_WeBoxEnabledAlLOWDownload = 1
test_tc_001_WeBoxEnabledAlLOWFileView = 1
test_tc_001_EnabledServiceTypes = 1
test_tc_001_WeBoxDisabledServiceTypes = 1
test_tc_001_WeBoxEnabledShowLinks = 1
test_tc_001_WeBoxEnabledOpenWith = 1
test_tc_001_DisabledWeBoxPasscode = 1
test_tc_001_EnabledWeBoxPasscode = 1
test_tc_001_EnabledGoogleDriveDropbox = 1
test_tc_001_AddingfoldersforSDcard = 1
test_tc_001_AddingfoldersforGoogleDrive = 1
test_tc_001_AddingfoldersforAmazonS3 = 1
test_tc_001_AddingfoldersforDropbox = 1
test_tc_001_EnabledSDcardAmazonS3 = 1
test_tc_001_DisabledSDcardAmazonS3 = 1
test_tc_001_DisabledGoogleDriveDropbox = 1
test_tc_001_DeletingfoldersforAmazonS3 = 1
test_tc_001_DeletingfoldersforGoogleDrive = 1
test_tc_001_DeletingfoldersforSDCard = 1
test_tc_001_DeletingfoldersforDropbox = 1
test_tc_001_DeviceUploads_GlobalSharedFolders = 1
test_tc_001_DeviceUploads_PolicyGroupsFolders = 1
test_tc_001_WeBox_DeviceUploads_pdf = 1
test_tc_001_WeBox_DeviceUploads_zip = 1
test_tc_001_DeviceUploads_CreateGlobalSharedFolders = 1
test_tc_001_DeviceUploads_CreatePolicyGroupsFolders = 1
test_tc_001_DeviceUploads_WeBoxuploadconfigingroupsfolder = 1
test_tc_001_DeviceUploads_PolicyGorupFolders_WeBoxuploadconfigwithsign = 1
test_tc_001_DeviceUploads_PolicyGorupFolders_WeBoxuploadconfigwithoutsign = 1
test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithsign = 1
test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithoutsign = 1
test_tc_001_DeviceUploads_WeBoxuploadconfiginglobalsharedfolder = 1
test_tc_001_DeviceUploads_GlobalSharedFolders_viewfilesinsharedfolder = 1
test_tc_001_DeviceUploads_PolicyGroupsFolders_viewfilesinpolicyfolder = 1
test_tc_001_DeviceUploads_GlobalSharedFolders_filesbyclickingonclearinsharedfolders = 1
test_tc_001_DeviceUploads_PolicyGroupsFolders_filesbyclickingonclearinpolicyfolders = 1
test_tc_001_DeviceUploads_SharedFolders_config = 1
test_tc_001_WeBox_SVGUpload = 1
test_tc_001_WeBox_MP3Upload = 1
test_tc_001_WeBox_MP4Upload = 1
test_tc_001_WeBox_OGGUpload = 1
test_tc_001_WeBox_TXTUpload = 1
test_tc_001_WeBox_DOCUpload = 1
test_tc_001_WeBox_DOCXUpload = 1
test_tc_001_WeBox_CSVUpload = 1
test_tc_001_WeBox_XLSXUpload = 1
test_tc_001_WeBox_WAVUpload = 1
test_tc_001_WeBox_APKUpload = 1
test_tc_001_WeBox_ZIPUpload = 1
test_tc_001_WeBox_GIFUpload = 1
test_tc_001_WeBox_JPGUpload = 1
test_tc_001_WeBox_MOVUpload = 1
test_tc_001_WeBox_PNGUpload = 1
test_tc_001_WeBox_PDFUpload = 1
test_tc_001_WeBox_PPTXUpload = 1
test_tc_001_WeBox_MPEGUpload = 1
test_tc_001_WeBox_WEBMUpload = 1
test_tc_001_GLobalLevel_UploadCertificate = 1
Filter_By_alldiffeventspolicy = 1

# Audit Logs
test_tc_901_AuditLogs_Filter_By_ALL = 1
test_tc_902_AuditLogs_Filter_By_All_Yesterday = 1
test_tc_903_AuditLogs_Filter_By_All_CustomDateRange = 1
test_tc_904_AuditLogs_Android_Device_Logs = 1
test_tc_905_AuditLogs_iOS_Device_Logs = 1
test_tc_906_AuditLogs_Windows_Device_Logs = 1


# Alerts Information
# Types are different and level is All
test_tc_1001_Alerts_Types_and_Levels_ALL = 1
test_tc_1002_Alerts_Levels= 1
test_tc_1003_Alerts_Types_and_Levels = 1
test_tc_1004_Unacknowledged_Alerts_CRITICAL = 1
test_tc_1005_Acknowledge_Alerts_CRITICAL = 1
test_tc_1006_TodaysAlerts = 1
test_tc_1007_YesterdaysAlerts = 1
test_tc_1008_CustomDateRange = 1

# Notification Microservice
test_1101_Notifications_AccountLevel_GET = 1
test_1102_Notifications_AccountLevel_POST = 1
test_1103_Notifications_AccountLevel_PUT = 1
test_1104_Notification_PolicyLevel_GET = 1
test_1105_NotificationServerVersion_GET = 1
test_1106_Notifications_PolicyLevel_POST = 1
test_1107_Notifications_PolicyLevel_PUT = 1
test_1108_Notification_PolicyLevel_Geofence_POST = 1
test_1109_Notification_PolicyLevel_Geofence_GET = 1
test_1110_Notification_PolicyLevel_Geofence_PUT = 1
test_1111_Notification_PolicyLevel_Geofence_DELETE = 0
test_1112_Notification_PolicyLevel_Geofence_Notifications_DELETE = 0
test_1113_Notification_PolicyLevel_Timespent_Geofence_POST = 1

def run_positive_tests():
    print("Inside run_positive_tests")

    global test_tc_01_Login
    test_tc_01_Login = 1

    global test_tc_1000_Logout
    test_tc_1000_Logout = 1

    global test_tc_000011_AccountLevel_Get_Alert_Configs
    test_tc_000011_AccountLevel_Get_Alert_Configs = 1


def run_negative_tests():
    print("Inside run_negative_tests")
    
    global test_tc_03_Invalid_credentials
    test_tc_000005_AccountAdmin_Invalid_credentials = 1

    global test_tc_04_Invalid_email
    test_tc_05_Invalid_email = 1

    global test_tc_06_Invalid_password
    test_tc_06_Invalid_password = 1

    global test_tc_07_Credentials_with_spaces
    test_tc_07_Credentials_with_spaces = 1

    global test_tc_000007_AccountAdmin_without_username
    test_tc_000007_AccountAdmin_without_username = 1

    global test_tc_000008_AccountAdmin_without_password
    test_tc_000008_AccountAdmin_without_password = 1

    global test_tc_000009_AccountAdmin_without_username_password
    test_tc_000009_AccountAdmin_without_username_password = 1


# Execute positive test cases
run_positive_tests()
run_negative_tests()
