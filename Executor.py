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
test_tc_1001_Login = 1
test_tc_1002_Login_Event = 1
test_tc_10000_Logout = 1

# Run all negative cases
test_tc_1003_AccountAdmin_Invalid_credentials = 1
test_tc_1004_AccountAdmin_Invalid_Email = 1
test_tc_1005_AccountAdmin_without_username = 1
test_tc_1006_AccountAdmin_Invalid_password = 1
test_tc_1007_AccountAdmin_without_password = 1
test_tc_1008_AccountAdmin_Invalid_password = 1

# Dashbord Page
test_tc_2001_Dashboard = 1
test_tc_2002_DashboardCalls = 1
test_tc_2003_DashboardRecentActivity = 1

# Devices Page
test_tc_3001_All_Devices_100 = 1
test_tc_3002_All_Devices_500 = 1
test_tc_3003_All_Devices_1000 = 1
test_tc_3004_Unenrolled_Devices = 1
test_tc_3005_Stolen_Devices = 1
test_tc_3006_Replaced_Devices = 1
test_tc_3007_Active_Devices = 1
test_tc_3008_Lost_Devices = 1
test_tc_3009_Unprovisioned_Devices = 1
test_tc_3010_Search_Policy = 1
test_tc_3011_Filter_By_GroupNames = 1
test_tc_3012_Enable_All_DevicesState = 1
test_tc_3013_Disable_All_DevicesState = 1
test_tc_3014_Android_Devices = 1
test_tc_3015_iOS_Devices = 1
test_tc_3016_Windows_Devices = 1

# Policy Groups
test_tc_4000_Policy_All=1

# Policy Groups -- Android Policy
test_tc_4001_GET_Android_Policy_By_ID = 1
test_tc_4002_GET_Android_AppsData = 1
test_tc_4003_GET_Android_Play_Store_AppsList = 1
test_tc_4004_GET_Android_Location_Track_Config = 1
test_tc_4005_GET_Android_DataUsage = 1
test_tc_4006_GET_Android_APN_Setting_ID = 1

# Device details view
test_tc_5001_GET_Android_Device_By_PolicyID=1
test_tc_5002_GET_Android_Device_By_MongoDBID=1
test_tc_5003_POST_Android_Device_FCMUpdate_DU=1
test_tc_5004_GET_Android_Device_Notes=1
test_tc_5005_POST_Android_Device_Activity=1
test_tc_5006_GET_Android_Device_ScreenShareHistory=1
test_tc_5007_GET_Android_Device_Apps=1
test_tc_5008_GET_Android_Device_Broadcast_History=1
test_tc_5009_PUT_Android_Device_Last_Contact_Time=1
test_tc_5010_GET_Android_Device_Data_Usage=1
test_tc_5011_GET_Android_Device_Enterprise_AppSizes=1
test_tc_5012_POST_Android_Device_Wake_Up=1
test_tc_5013_POST_Android_AuthToken_ConnectToDevice=1
test_tc_5014_POST_Android_FCMUpdate_RemoteView_LiveView=1
test_tc_5015_POST_Android_ScreenShareHistory_LiveView=1
test_tc_5016_GET_Android_Device_WebRTCScreenShareHistory=1
test_tc_5017_POST_Android_Device_AcknowledgeEventLogs_LiveView=1
test_tc_5018_POST_Android_Device_TagsIDs=1
test_tc_5019_POST_Android_Device_Notes=1
# Data Usage - Clicking on the Refresh icon
test_tc_5020_POST_Android_Device_DataUsage=1

# Device Commands
test_tc_5021_Android_Device_Commands=0
test_tc_5022_Android_Device_Admin_Device_Commands=0


# Enterprise App Version
test_1111111_Enterprise_Server_Version_GET=1

# Windows Microservices
# Windows Device
test_tc_0000001_Windows_DeviceDetailsByMongoID_GET = 1
test_tc_0000002_Windows_Device_Updates_Tags_By_MongoID_PUT = 1
test_tc_0000003_Windows_Fetch_Device_Details_GET = 1
test_tc_0000004_Windows_Fetch_Devices_By_PolicyIDs_POST=1
test_tc_0000005_Windows_Add_Device_Commands_POST=1
test_tc_0000006_Windows_Device_Last_Contact_Time_PUT=1
test_tc_0000007_Windows_DeviceDetailsByPolicyID_GET =1
test_tc_0000008_Windows_Device_Search_By_PolicyID_GET =1
test_tc_0000009_Windows_Device_Search_By_All_String_GET=1
# Windows Policy
test_tc_1100001_Windows_Policy_Clone_POST=1
test_tc_1100002_Windows_Policy_Delete=1
test_tc_1100003_Windows_Policy_GET=1

# CSPs
test_tc_1170001_Windows_Generic_CSPs_POST = 1

# Contacts
test_tc_14000_Create_Contacts_Account_Level_POST = 1
test_tc_14001_Contacts_Account_Level_FCM_UPDATE_After_CreatingAdding_Contacts_POST = 1
test_tc_14002_Contacts_Account_Level_POST = 1
test_tc_14003_Contacts_Account_Level_DELETE = 1
test_tc_14004_Contacts_Account_Level_FCM_UPDATE_POST = 1
test_tc_14005_Create_Contacts_Policy_Level_POST = 1
test_tc_14006_Contacts_Policy_Level_FCM_UPDATE_After_CreatingAdding_Contacts_POST = 1
test_tc_14007_Contacts_Policy_Level_POST = 1
test_tc_14008_Contacts_Policy_Level_DELETE = 1
test_tc_14009_Contacts_Policy_Level_FCM_UPDATE_POST = 1


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
test_1105_Notification_Server_Version_GET = 1
test_1106_Notifications_PolicyLevel_POST = 1
test_1107_Notifications_PolicyLevel_PUT = 1
test_1108_Notification_PolicyLevel_Geofence_POST = 1
test_1109_Notification_PolicyLevel_Geofence_GET = 1
test_1110_Notification_PolicyLevel_Geofence_PUT = 1
test_1111_Notification_PolicyLevel_Geofence_DELETE = 1
test_1112_Notification_PolicyLevel_Geofence_Notifications_DELETE = 0
test_1113_Notification_Timespent_Geofence_ALL_Policies_Device_Geofences_POST = 1

def run_positive_tests():
    print("Inside run_positive_tests")

    global test_tc_1001_Login
    test_tc_1001_Login = 1

    global test_tc_10000_Logout
    test_tc_10000_Logout = 1


def run_negative_tests():
    print("Inside run_negative_tests")
    
    global test_tc_1003_AccountAdmin_Invalid_credentials
    test_tc_1003_AccountAdmin_Invalid_credentials = 1

    global test_tc_1004_AccountAdmin_Invalid_Email
    test_tc_1004_AccountAdmin_Invalid_Email = 1

    global test_tc_1005_AccountAdmin_without_username
    test_tc_1005_AccountAdmin_without_username = 1
    
    global test_tc_1007_AccountAdmin_without_password
    test_tc_1007_AccountAdmin_without_password = 1
    
    global test_tc_1008_AccountAdmin_Invalid_password
    test_tc_1008_AccountAdmin_Invalid_password = 1



# Execute positive test cases
run_positive_tests()
run_negative_tests()
