from datetime import datetime
import requests
import pytest
import globalvariables
import general_payload
import Logs as WeGuard
import Executor as Execute
import test_GETutils as Utils


def AuditLogs(page, size):
    allLogs = "enterprise/rest/weguard/logs/eventsPerAccount?page={page}&size={size}".format(page=page, size=size)
    return allLogs


# # Filter By Level = All, Filter By Events = All and Date Range is current (today)
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_901_AuditLogs_Filter_By_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.auditlogs
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10251)
# def test_tc_0001_Filter_By_Level_and_Event_ALL_on_CurrentDateTime(url):
#     Log_Levels = ["All", "Info", "Warn", "Debug", "Error"]
#     Events = ["All", "Login", "Logout", "Start Impersonate", "End Impersonate", "Policy", "Device", "Group", "Upload",
#               "Roles and Permissions", "Command", "Broadcast", "WeTalk", "WeBox passcode", "Kiosk passcode", "USERNAME",
#               "META DATA", "KIOSK", "EMM_ACCOUNT", "LOCATION", "POLICY", "APPLICATION", "SERVICES", "KNOX",
#               "CRASH REPORT EVENT", "PROVISIONING", "KIOSK LOCK/UNLOCK EVENT", "DEVICE LOCK EVENT", "POLL EVENT",
#               "GET LICENSE", "PROVISION PROFILE LICENSE", "LICENSE ACTIVATION", "DEVICE WIPE EVENT", "DATA USAGE EVENT",
#               "PUSH EVENTS", "WeGuard APP", "Find my device", "OTHER EVENTS", "OPS", "DeviceInformation",
#               "ClearPasscode", "DeviceLock", "InstallApplication", "RemoveApplication", "InstallProfile",
#               "InstallProvisioningProfile", "Settings", "RestartDevice", "ShutDownDevice"]
#
#     def generate_test_cases():
#         test_cases = []
#         for level in Log_Levels:
#             for event in Events:
#                 test_cases.append((level, event))
#         return test_cases
#
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for LogLevel, Event in generate_test_cases():
#             apiUrl = globalvariables.BaseURL + AuditLogs(globalvariables.page_1, globalvariables.page_100)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#             payload = {
#                 "startDate": globalvariables.start_timestamp,
#                 "endDate": globalvariables.end_timestamp,
#                 "event": Event,
#                 "logLevel": LogLevel,
#                 "deviceIds": [],
#                 "policyIds": None
#             }
#             res = requests.post(url=apiUrl, headers=Headers, json=payload, timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" +"\n")
#                 # Print information about the current test case
#                 print(f"Test Case: Filter By Level = {LogLevel}, Filter By Event = {Event}" + "\n")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "500 Result not found!")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Failed -- Filter By Level = All, Filter By Events = All and Date Range is current (today) ---------------------------\n")
#         assert False
#
# # Filter By Level = All and Date Range is Yesterday
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_902_AuditLogs_Filter_By_All_Yesterday == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.auditlogs
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10252)
# def test_tc_0002_Filter_By_All_Yesterday(url):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvariables.BaseURL + AuditLogs(globalvariables.page_1, globalvariables.page_1000)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=general_payload.AllYesterdayLogs, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n\n-------- Filter By Level = All and Date Range is Yesterday --------")
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "500 Result not found!")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("\n\n--------  Failed -- Filter By Level = All and Date Range is Yesterday --------")
#         assert False
#
# # Filter By Level = All and Date Range is Custom (1 Month)
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_903_AuditLogs_Filter_By_All_CustomDateRange == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.auditlogs
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10253)
# def test_tc_0003_Filter_By_All_Custom_1Month(url):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvariables.BaseURL + AuditLogs(globalvariables.page_1, globalvariables.page_1000)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=general_payload.AllCustom1MonthLogs, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n\n-------- Filter By Level = All and Date Range is Custom (1 Month) --------")
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             WeGuard.logger.debug("\n" + "200 The request was a success!" + "\n")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "500 Result not found!")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("\n\n--------  Failed -- Filter By Level = All and Date Range is Custom (1 Month) --------")
#         assert False

# Fetch Android Device Logs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_904_AuditLogs_Android_Device_Logs == 0,
                    reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10254)
def test_tc_0004_Android_Device_Logs(url):
    now1 = datetime.now()
    if globalvariables.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for android_device_id in globalvariables.Android_DeviceIDs:
            print(f"Processing Android devices: {android_device_id}")
            apiUrl = globalvariables.BaseURL + AuditLogs(globalvariables.page_1, globalvariables.page_1000)
            Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
            Android_payload = {
                "startDate": globalvariables.start_timestamp,
                "endDate": globalvariables.end_timestamp,
                "event": "All",
                "logLevel": "All",
                "deviceIds": [android_device_id],
                "policyIds": None
            }
            print(Android_payload)
            res = requests.post(url=apiUrl, headers=Headers, json=Android_payload, timeout=globalvariables.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!" +"\n")
                # Print information about the current test case
                print(f" Android Device logs are fetched" + "\n")
                print("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "500 Result not found!")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error(f"Android Device logs are not fetched" + "\n")
        assert False

# Fetch iOS Device Logs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_905_AuditLogs_iOS_Device_Logs == 0,
                    reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10255)
def test_tc_0005_iOS_Device_Logs(url):
    now1 = datetime.now()
    if globalvariables.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for iOS_device_id in globalvariables.iOS_DeviceIDs:
            print(f"Processing iOS devices: {iOS_device_id}")
            apiUrl = globalvariables.BaseURL + AuditLogs(globalvariables.page_1, globalvariables.page_1000)
            Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
            iOS_payload = {
                "startDate": globalvariables.start_timestamp,
                "endDate": globalvariables.end_timestamp,
                "event": "All",
                "logLevel": "All",
                "deviceIds": [iOS_device_id],
                "policyIds": None
            }
            res = requests.post(url=apiUrl, headers=Headers, json=iOS_payload, timeout=globalvariables.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!" +"\n")
                # Print information about the current test case
                print(f" iOS Device logs are fetched" + "\n")
                print("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "500 Result not found!")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error(f"iOS Device logs are not fetched" + "\n")
        assert False

# Fetch Windows Device Logs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_906_AuditLogs_Windows_Device_Logs == 0,
                    reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10256)
def test_tc_0006_Windows_Device_Logs(url):
    now1 = datetime.now()
    if globalvariables.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Windows_device_id in globalvariables.Windows_DeviceIDs:
            print(f"Processing Windows devices: {Windows_device_id}")
            apiUrl = globalvariables.BaseURL + AuditLogs(globalvariables.page_1, globalvariables.page_1000)
            Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
            Windows_payload = {
                "startDate": globalvariables.start_timestamp,
                "endDate": globalvariables.end_timestamp,
                "event": "All",
                "logLevel": "All",
                "deviceIds": [Windows_device_id],
                "policyIds": None
            }
            res = requests.post(url=apiUrl, headers=Headers, json=Windows_payload, timeout=globalvariables.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!" +"\n")
                # Print information about the current test case
                print(f"Windows Device logs are fetched" + "\n")
                print("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "500 Result not found!")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error(f"Windows Device logs are not fetched" + "\n")
        assert False
