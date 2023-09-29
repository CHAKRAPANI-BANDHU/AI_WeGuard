from datetime import datetime

import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import general_payload as GeneralPayload


def AndroidDeviceByPolicyID(policyId):
    return "enterprise/rest/weguard-v2/policy/{policyId}".format(policyId=policyId)


def AndroidDeviceByMongoDBID(mongoDBId):
    return "enterprise/rest/v3/device/android/{mongoDBId}".format(mongoDBId=mongoDBId)


FCMUpdate = "enterprise/rest/weguard-v2/fcmUpdate"


def AndroidNotesGET(androidDeviceID, page, limit):
    return "enterprise/rest/notes/{androidDeviceID}?page={page}&limit={limit}".format(androidDeviceID=androidDeviceID,
                                                                                      page=page, limit=limit)


def AndroidActivity(page, size):
    allLogs = "enterprise/rest/weguard/logs/eventsPerAccount?page={page}&size={size}".format(page=page, size=size)
    return allLogs


def ScreenShareHistory(AndroidDeviceID, page, size, email):
    return ("enterprise/rest/webrtc/screensharehistory/{AndroidDeviceID}?"
            "page={page}&pageSize={size}&email={email}").format(
        AndroidDeviceID=AndroidDeviceID, page=page, size=size, email=email)


def AndroidDeviceApps(AndroidDeviceID):
    return "enterprise/rest/deviceapps/apps/{AndroidDeviceID}".format(AndroidDeviceID=AndroidDeviceID)


def AndroidDeviceBroadcastHistory(AndroidDeviceID, page, pageSize):
    return "enterprise/rest/broadcast/history/device/{AndroidDeviceID}?pageNo={page}&pageSize={pageSize}&type=FCM_MESSAGE".format(
        AndroidDeviceID=AndroidDeviceID, page=page, pageSize=pageSize)


AndroidDeviceLastContactTime = "enterprise/rest/v3/device/last-contact-time"


def AndroidDeviceDataUsage(AndroidDeviceID):
    return "enterprise/rest/app/device/{AndroidDeviceID}".format(AndroidDeviceID=AndroidDeviceID)


def AndroidDeviceEnterpriseAppSizes(AndroidDeviceID, AndroidDeviceMongoDBID):
    return "enterprise/rest/apkdownload/{AndroidDeviceID}/{AndroidDeviceMongoDBID}".format(
        AndroidDeviceID=AndroidDeviceID, AndroidDeviceMongoDBID=AndroidDeviceMongoDBID)


WeSupportAuthToken = "enterprise/rest/wetalk/video/authtoken"

# When device is offline
AbortedDeviceScreenShareHistory = "enterprise/rest/webrtc/screensharehistory"

# After acknowledging the live view request on device
WeSupportEventLogs = "enterprise/rest/weguard/logs/events"

# Tags/IDs, POST Notes, Wipe Device, Uninstall WeGuard app
UpdateDevice = "enterprise/rest/weguard-v2/updateDevice"

# Admin Lock/Unlock
Actions = "enterprise/rest/v3/device/action"

# Device Commands
Device_Commands = ["RESTART_DEVICE", "POWER_OFF_DEVICE", "LOCK_DEVICE", "UNLOCK_DEVICE", "KIOSK_PASSWORD_RESET_DEVICE"]
Admin_Device_Commands = ["ADMIN_LOCK", "ADMIN_UNLOCK"]


# GET -- Clicking on Android Device ID (get details by policyID)
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5001_GET_Android_Device_By_PolicyID == 0,
                    reason="GET Android Device by MongoDB ID is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50001)
def test_tc_5001_Android_Device_By_PolicyID_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for policy_id in globalvar.Android_Policy_IDs:
            apiUrl = globalvar.BaseURL + AndroidDeviceByPolicyID(policy_id)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device by policy ID) ---------------------------\n\n")
        assert False


# GET -- Clicking on Android Device ID (get details by Mongo DB ID)
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5002_GET_Android_Device_By_MongoDBID == 0,
                    reason="GET Android Device by MongoDB ID is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50002)
def test_tc_5002_Android_Device_By_MongoDBID_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for mongoDBID in globalvar.Android_Mongo_DB_DeviceIDs:
            apiUrl = globalvar.BaseURL + AndroidDeviceByMongoDBID(mongoDBID)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device by MongoDB ID ---------------------------\n\n")
        assert False


# POST -- FCM Update of APK DU
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5003_POST_Android_Device_FCMUpdate_DU == 0, reason="FCM Update APK DU is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50003)
def test_tc_5003_Android_Device_APK_DU_FCMUpdate(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            for policyID in globalvar.Android_Policy_IDs:
                apiUrl = globalvar.BaseURL + FCMUpdate
                Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
                APKDUPayload = {
                    "topic": Android_DeviceID + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
                    "type": "FCM_APK_DU", "isLicenseLevel": False,
                    "pId": policyID, "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode,
                    "priority": "high"}
                res = requests.post(url=apiUrl, headers=Headers, json=APKDUPayload, timeout=globalvar.timeout)
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                if res.status_code == 200:
                    print("\n" + "200 The request was a success!")
                    print(  # "\n" + "Header: " + str(res.headers) + "\n"
                        "\n" + "Request URL: " + apiUrl +
                        "\n" + "Request Method: " + res.request.method +
                        "\n" + "Status Code: " + str(res.status_code) +
                        "\n" + "Request Payload: " + str(APKDUPayload) +
                        "\n" + "Response: " + str(res.content) + "\n")
                elif res.status_code == 400:
                    print("\n" + "400 Bad Request!" + "\n")
                    # Add your assertions or actions for 400 Bad Request response here
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n" + "404 Result not found!" + "\n")
                    # Add your assertions or actions for 404 Not Found response here
                    assert False, "Received 404 response"
                elif res.status_code == 500:
                    print("\n" + "500 Internal Server Error!" + "\n")
                    # Add your assertions or actions for 500 Internal Server Error response here
                    assert False, "Received 500 response"
                else:
                    print("Request did not succeed! Status code:", res.status_code)
                    assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to FCM Update for APK DU ---------------------------\n\n")
        assert False


# GET -- Get Notes for Android Devices
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5004_GET_Android_Device_Notes == 0,
                    reason="GET Android Device Notes is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50004)
def test_tc_5004_Android_Device_Notes_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + AndroidNotesGET(AndroidDeviceID, globalvar.page_1, globalvar.page_500)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Notes ---------------------------\n\n")
        assert False


# GET Android Activity Logs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5005_POST_Android_Device_Activity == 0,
                    reason="Android Device Logs in device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.devicedetailsview
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=50005)
def test_tc_5005_Android_Device_Logs(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for android_device_id in globalvar.Android_DeviceIDs:
            print(f"Processing Android devices: {android_device_id}")
            apiUrl = globalvar.BaseURL + AndroidActivity(globalvar.page_1, globalvar.page_1000)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            Android_payload = {
                "startDate": globalvar.start_timestamp,
                "endDate": globalvar.end_timestamp,
                "event": "All",
                "logLevel": "All",
                "deviceIds": [android_device_id],
                "policyIds": None
            }
            print(Android_payload)
            res = requests.post(url=apiUrl, headers=Headers, json=Android_payload, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!" + "\n")
                # Print information about the current test case
                print(f" Android Device logs are fetched" + "\n")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(Android_payload) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(f"Android Device logs are not fetched" + "\n")
        assert False


# GET -- Get Screen Share History of Android Device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5006_GET_Android_Device_ScreenShareHistory == 0,
                    reason="GET Android Device Screen Share History is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50006)
def test_tc_5006_Android_ScreenShareHistory_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + ScreenShareHistory(AndroidDeviceID, globalvar.page_1, globalvar.page_500,
                                                            globalvar.userName)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Screen Share History ---------------------------\n\n")
        assert False


# GET -- Android Device Apps
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5007_GET_Android_Device_Apps == 0,
                    reason="GET Android Device Apps is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50007)
def test_tc_5007_Android_Device_Apps_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + AndroidDeviceApps(AndroidDeviceID)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Apps ---------------------------\n\n")
        assert False


# GET -- Android Device Broadcast History
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5008_GET_Android_Device_Broadcast_History == 0,
                    reason="GET Android Device Broadcast History is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50008)
def test_tc_5008_Android_Device_Broadcast_History_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + AndroidDeviceBroadcastHistory(AndroidDeviceID, globalvar.page_1,
                                                                       globalvar.page_500)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Broadcast History ---------------------------\n\n")
        assert False


# PUT -- Android Device Last Contact Time
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5009_PUT_Android_Device_Last_Contact_Time == 0,
                    reason="PUT Android Device Last Contact Time is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50009)
def test_tc_5009_Android_Device_Last_Contact_Time_PUT(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + AndroidDeviceLastContactTime
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            LastContactTimeAndroidPayload = {"deviceId": AndroidDeviceID, "lastContactTime": globalvar.isostart}
            res = requests.put(url=apiUrl, headers=Headers, json=LastContactTimeAndroidPayload,
                               timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(LastContactTimeAndroidPayload) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Last Contact Time ---------------------------\n\n")
        assert False


# GET -- Android Device Broadcast History
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5010_GET_Android_Device_Data_Usage == 0,
                    reason="GET Android Device Data Usage is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50010)
def test_tc_5010_Android_Device_Data_Usage_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + AndroidDeviceDataUsage(AndroidDeviceID)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Data Usage ---------------------------\n\n")
        assert False


# GET -- Android Device Broadcast History
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5011_GET_Android_Device_Enterprise_AppSizes == 0,
                    reason="GET Android Device Enterprise App Sizes is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50011)
def test_tc_5011_Android_Device_Enterprise_AppSizes_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            for AndroidDeviceMongoID in globalvar.Android_Mongo_DB_DeviceIDs:
                apiUrl = globalvar.BaseURL + AndroidDeviceEnterpriseAppSizes(AndroidDeviceID, AndroidDeviceMongoID)
                Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
                res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                if res.status_code == 200:
                    print("\n" + "200 The request was a success!")
                    print(  # "\n" + "Header: " + str(res.headers) + "\n"
                        "\n" + "Request URL: " + apiUrl +
                        "\n" + "Request Method: " + res.request.method +
                        "\n" + "Status Code: " + str(res.status_code) +
                        "\n" + "Response: " + str(res.content) + "\n")
                elif res.status_code == 400:
                    print("\n" + "400 Bad Request!" + "\n")
                    # Add your assertions or actions for 400 Bad Request response here
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n" + "404 Result not found!" + "\n")
                    # Add your assertions or actions for 404 Not Found response here
                    assert False, "Received 404 response"
                elif res.status_code == 500:
                    print("\n" + "500 Internal Server Error!" + "\n")
                    # Add your assertions or actions for 500 Internal Server Error response here
                    assert False, "Received 500 response"
                else:
                    print("Request did not succeed! Status code:", res.status_code)
                    assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device Enterprise App Sizes ---------------------------\n\n")
        assert False


# POST -- FCM Update of Device Wake Up
# When device is Offline and clicking on device id
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5012_POST_Android_Device_Wake_Up == 0,
                    reason="FCM Update Device Wake Up is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50012)
def test_tc_5012_Android_Device_Wake_Up_FCMUpdate_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            for policyID in globalvar.Android_Policy_IDs:
                apiUrl = globalvar.BaseURL + FCMUpdate
                Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
                DeviceWakeUpPayload = {
                    "topic": Android_DeviceID + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
                    "type": "DEVICE_WAKEUP", "priority": "high", "isLicenseLevel": False,
                    "pId": policyID, "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode}
                res = requests.post(url=apiUrl, headers=Headers, json=DeviceWakeUpPayload, timeout=globalvar.timeout)
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                if res.status_code == 200:
                    print("\n" + "200 The request was a success!")
                    print(  # "\n" + "Header: " + str(res.headers) + "\n"
                        "\n" + "Request URL: " + apiUrl +
                        "\n" + "Request Method: " + res.request.method +
                        "\n" + "Status Code: " + str(res.status_code) +
                        "\n" + "Request Payload: " + str(DeviceWakeUpPayload) +
                        "\n" + "Response: " + str(res.content) + "\n")
                elif res.status_code == 400:
                    print("\n" + "400 Bad Request!" + "\n")
                    # Add your assertions or actions for 400 Bad Request response here
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n" + "404 Result not found!" + "\n")
                    # Add your assertions or actions for 404 Not Found response here
                    assert False, "Received 404 response"
                elif res.status_code == 500:
                    print("\n" + "500 Internal Server Error!" + "\n")
                    # Add your assertions or actions for 500 Internal Server Error response here
                    assert False, "Received 500 response"
                else:
                    print("Request did not succeed! Status code:", res.status_code)
                    assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to FCM Update for Device Wake Up ---------------------------\n\n")
        assert False


# Test case for Live View
# Click on Connect to Device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5013_POST_Android_AuthToken_ConnectToDevice == 0,
                    reason="AuthToken for WeSupport is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50018)
def test_tc_5013_Android_Device_ConnectToDevice_AuthToken(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + WeSupportAuthToken
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            AuthTokenPayload = {
                "roomId": "WESUPPORT" + "_" + Android_DeviceID,
                "identify": globalvar.userName + "::" + GeneralPayload.Room_ID,
                "roomType": "peer-to-peer"}
            res = requests.post(url=apiUrl, headers=Headers, json=AuthTokenPayload, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(AuthTokenPayload) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to Create Auth Token (WeSupport - Connect to Device) ---------------------------\n\n")
        assert False


# POST -- FCM Update of Remote View
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5014_POST_Android_FCMUpdate_RemoteView_LiveView == 0,
                    reason="FCM Update Remote View is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50014)
def test_tc_5014_Android_Device_RemoteView_FCMUpdate_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + FCMUpdate
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            FCMRemoteViewPayload = {
                "topic": Android_DeviceID + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
                "type": "FCM_REMOTE_VIEW", "isLicenseLevel": False, "actCode": globalvar.activationCode,
                "pActCode": globalvar.productActivationCode, "message": "{\"liveSupportMode\":1}",
                "timestamp": globalvar.start_timestamp, "id": GeneralPayload.RandomID}
            res = requests.post(url=apiUrl, headers=Headers, json=FCMRemoteViewPayload, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(FCMRemoteViewPayload) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to FCM Update for Remote View ---------------------------\n\n")
        assert False


# POST -- Screen Share History of Aborted Device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5015_POST_Android_ScreenShareHistory_LiveView == 0,
                    reason="Device screen share history is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50015)
def test_tc_5015_Android_Device_ScreenShareHistory(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + AbortedDeviceScreenShareHistory
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            DeviceScreenShareHistoryPayload = {
                "sessionId": GeneralPayload.SessionID, "deviceId": Android_DeviceID, "actor": globalvar.userName,
                "status": "Aborted", "role": globalvar.role, "topic": "WESUPPORT" + "_" + Android_DeviceID,
                "postLog": True,
                "startTime": globalvar.start_timestamp, "endTime": globalvar.end_timestamp, "totalBytesReceived": None,
                "totalBytesSent": None,
                "date": globalvar.end_timestamp
            }
            res = requests.post(url=apiUrl, headers=Headers, json=DeviceScreenShareHistoryPayload,
                                timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(DeviceScreenShareHistoryPayload) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display screen share history ---------------------------\n\n")
        assert False


# GET -- Get WebRTC Screen Share History of Android Device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5016_GET_Android_Device_WebRTCScreenShareHistory == 0,
                    reason="GET Android Device WebRTC Screen Share History is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50016)
def test_tc_5016_Android_ScreenShareHistory_WebRTC_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + ScreenShareHistory(AndroidDeviceID, globalvar.page_1, globalvar.page_500,
                                                            globalvar.userName)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the Android Device WebRTC Screen Share History ---------------------------\n\n")
        assert False


# POST -- Event Logs after accepting the request on the device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5017_POST_Android_Device_AcknowledgeEventLogs_LiveView == 0,
                    reason="Live view of device is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50017)
def test_tc_5017_Android_Device_Live_View(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidPolicyID in globalvar.Android_Policy_IDs:
            apiUrl = globalvar.BaseURL + WeSupportEventLogs
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            EventLogs = {
                "agent": "PORTAL", "actorId": globalvar.userName, "policyId": AndroidPolicyID, "type": "", "msg": "",
                "action": "WeSupport started", "event": "LIVE VIEW", "sentTime": globalvar.start_timestamp,
                "sourceIP": "",
                "logLevel": "Info", "log": "WeSupport session started for the device In-House",
                "activationCode": globalvar.activationCode, "productActivationCode": globalvar.productActivationCode,
                "metadata": {"name": globalvar.name}
            }
            res = requests.post(url=apiUrl, headers=Headers, json=EventLogs, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(EventLogs) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the event logs of live view request acknowledge on device ---------------------------\n\n")
        assert False


# Tags/IDs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5018_POST_Android_Device_TagsIDs == 0,
                    reason="Android Tags/IDs is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50018)
def test_tc_5018_Android_Device_TagsIDs(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            apiUrl = globalvar.BaseURL + UpdateDevice
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            TagsIDs = {"activationCode": globalvar.activationCode,
                       "productActivationCode": globalvar.productActivationCode,
                       "updateDeviceRequest": [
                           {"deviceID": AndroidDeviceID, "id1": "QA Team", "id2": "1201" + str(GeneralPayload.RandomID),
                            "id3": None,
                            "adminTaggedName": "In-House", "simLockPin": None, "resetPassword": None,
                            "enableWeguardUninstall": False}]}
            res = requests.post(url=apiUrl, headers=Headers, json=TagsIDs, timeout=globalvar.timeout)
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Request Payload: " + str(TagsIDs) +
                    "\n" + "Response: " + str(res.content) + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to updated the Android Tags/IDs ---------------------------\n\n")
        assert False


# POST -- create a note for Android Devices
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5019_POST_Android_Device_Notes == 0,
                    reason="POST Android Device Create Notes is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50019)
def test_tc_5019_Android_Device_Notes_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AndroidDeviceID in globalvar.Android_DeviceIDs:
            for policyID in globalvar.Android_Policy_IDs:
                apiUrl = globalvar.BaseURL + UpdateDevice
                Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
                NotesPayload = {"deviceId": AndroidDeviceID, "note": GeneralPayload.randomName,
                                "policyId": policyID,
                                "activation": globalvar.activationCode, "type": "General",
                                "deviceType": "ANDROID"}
                res = requests.post(url=apiUrl, headers=Headers, json=NotesPayload, timeout=globalvar.timeout)
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                if res.status_code == 200:
                    print("\n" + "200 The request was a success!")
                    print(  # "\n" + "Header: " + str(res.headers) + "\n"
                        "\n" + "Request URL: " + apiUrl +
                        "\n" + "Request Method: " + res.request.method +
                        "\n" + "Status Code: " + str(res.status_code) +
                        "\n" + "Request Payload: " + str(NotesPayload) +
                        "\n" + "Response: " + str(res.content) + "\n")
                elif res.status_code == 400:
                    print("\n" + "400 Bad Request!" + "\n")
                    # Add your assertions or actions for 400 Bad Request response here
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n" + "404 Result not found!" + "\n")
                    # Add your assertions or actions for 404 Not Found response here
                    assert False, "Received 404 response"
                elif res.status_code == 500:
                    print("\n" + "500 Internal Server Error!" + "\n")
                    # Add your assertions or actions for 500 Internal Server Error response here
                    assert False, "Received 500 response"
                else:
                    print("Request did not succeed! Status code:", res.status_code)
                    assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to create a note for the Android Device ---------------------------\n\n")
        assert False


# Data Usage - Click on the refresh icon
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_5020_POST_Android_Device_DataUsage == 0,
                    reason="FCM Update Data Usage is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50020)
def test_tc_5020_Android_Device_DataUsage_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            for policyID in globalvar.Android_Policy_IDs:
                apiUrl = globalvar.BaseURL + FCMUpdate
                Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
                ReadDataUsagePayload = {
                    "topic": Android_DeviceID + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
                    "type": "READ_DATA_USAGE", "isLicenseLevel": False,
                    "pId": policyID, "actCode": globalvar.activationCode,
                    "pActCode": globalvar.productActivationCode, "priority": "high",
                    "id": GeneralPayload.RandomContactsIDs}
                res = requests.post(url=apiUrl, headers=Headers, json=ReadDataUsagePayload, timeout=globalvar.timeout)
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                if res.status_code == 200:
                    print("\n" + "200 The request was a success!")
                    print(  # "\n" + "Header: " + str(res.headers) + "\n"
                        "\n" + "Request URL: " + apiUrl +
                        "\n" + "Request Method: " + res.request.method +
                        "\n" + "Status Code: " + str(res.status_code) +
                        "\n" + "Request Payload: " + str(ReadDataUsagePayload) +
                        "\n" + "Response: " + str(res.content) + "\n")
                elif res.status_code == 400:
                    print("\n" + "400 Bad Request!" + "\n")
                    # Add your assertions or actions for 400 Bad Request response here
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n" + "404 Result not found!" + "\n")
                    # Add your assertions or actions for 404 Not Found response here
                    assert False, "Received 404 response"
                elif res.status_code == 500:
                    print("\n" + "500 Internal Server Error!" + "\n")
                    # Add your assertions or actions for 500 Internal Server Error response here
                    assert False, "Received 500 response"
                else:
                    print("Request did not succeed! Status code:", res.status_code)
                    assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to FCM Update for Data usage ---------------------------\n\n")
        assert False


# Device Commands
@pytest.mark.parametrize('device_command', Device_Commands)
@pytest.mark.skipif(Execute.test_tc_5021_Android_Device_Commands == 0,
                    reason="Device Commands is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
def test_tc_5021_Android_Device_Reboot(device_command):
    now1 = datetime.now()
    if not globalvar.bearerToken:
        pytest.skip("Empty Bearer token. Skipping test.")
    
    try:
        for Android_DeviceID in globalvar.Android_DeviceIDs:
            for policyID in globalvar.Android_Policy_IDs:
                apiUrl = globalvar.BaseURL + FCMUpdate
                Headers = {'Authorization': f'Bearer {globalvar.bearerToken}'}
                device_command_payload = {
                    "topic": f"{Android_DeviceID}_{globalvar.activationCode}_{globalvar.productActivationCode}",
                    "type": device_command, "isLicenseLevel": False, "pId": policyID,
                    "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode,
                    "priority": "high", "id": GeneralPayload.RandomContactsIDs}
                res = requests.post(url=apiUrl, headers=Headers, json=device_command_payload, timeout=globalvar.timeout)
                if res.status_code == 200:
                    print("\n200 The request was a success!")
                    # Print request and response details
                    curl_str = Utils.getCurlEquivalent(res)
                    print(curl_str)
                    print(
                        f"\nRequest URL: {apiUrl}\n"
                        f"Request Method: {res.request.method}\n"
                        f"Status Code: {res.status_code}\n"
                        f"Request Payload: {device_command_payload}\n"
                        f"Response: {res.content}\n")
                elif res.status_code == 400:
                    print("\n400 Bad Request!")
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n404 Result not found!")
                    assert False, "Received 404 Not Found response"
                elif res.status_code == 500:
                    print("\n500 Internal Server Error!")
                    assert False, "Received 500 Internal Server Error response"
                else:
                    print(f"Request did not succeed! Status code: {res.status_code}")
                    assert False, f"Received {res.status_code} response"
    except Exception as e:
        print(f"Exception: {str(e)}")
        now2 = datetime.now()
        print(f"Time taken: {str(now2 - now1)}")
        print(f"\nExecuted the Device Command = {device_command}\n")


# Admin Lock
@pytest.mark.parametrize('admin_device_command', Admin_Device_Commands)
@pytest.mark.skipif(Execute.test_tc_5022_Android_Device_Admin_Device_Commands == 0,
                    reason="Admin Device Commands is skipped")
@pytest.mark.positivetest
@pytest.mark.devicedetailsview
@pytest.mark.regressiontest
@pytest.mark.run(order=50022)
def test_tc_5022_Android_Device_Admin_Device_Commands(admin_device_command):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for AdminCommand in Admin_Device_Commands:
            for Android_DeviceID in globalvar.Android_DeviceIDs:
                apiUrl = globalvar.BaseURL + Actions
                Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
                AdminDeviceCommandsPayload = {"action": AdminCommand, "deviceIds": [Android_DeviceID],
                                              "msg": "Please contact the Administrator",
                                              "adminLockScheduleTimestamp": globalvar.start_timestamp}
                res = requests.post(url=apiUrl, headers=Headers, json=AdminDeviceCommandsPayload,
                                    timeout=globalvar.timeout)
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                if res.status_code == 200:
                    print("\n" + "200 The request was a success!")
                    print(
                        f"\n------------------- Executed the Device Command = {admin_device_command} ---------------------------\n")
                    print(
                        "\n" + "Request URL: " + apiUrl +
                        "\n" + "Request Method: " + res.request.method +
                        "\n" + "Status Code: " + str(res.status_code) +
                        "\n" + "Request Payload: " + str(AdminDeviceCommandsPayload) +
                        "\n" + "Response: " + str(res.content) + "\n"
                    )
                elif res.status_code == 400:
                    print("\n" + "400 Bad Request!" + "\n")
                    # Add your assertions or actions for 400 Bad Request response here
                    assert False, "Received 400 Bad Request response"
                elif res.status_code == 404:
                    print("\n" + "404 Result not found!" + "\n")
                    # Add your assertions or actions for 404 Not Found response here
                    assert False, "Received 404 response"
                elif res.status_code == 500:
                    print("\n" + "500 Internal Server Error!" + "\n")
                    # Add your assertions or actions for 500 Internal Server Error response here
                    assert False, "Received 500 response"
                else:
                    print("Request did not succeed! Status code:", res.status_code)
                    assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception: " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            f"\n------------------- Failed to execute the Device Command = {admin_device_command} ---------------------------\n")
        assert False
