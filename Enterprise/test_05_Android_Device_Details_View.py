# from datetime import datetime
#
# import pytest
# import requests
# import globalvariables as globalvar
# import Executor as Execute
# import test_GETutils as Utils
#
#
# def AndroidDeviceByPolicyID(policyId):
#     return "enterprise/rest/weguard-v2/policy/{policyId}".format(policyId=policyId)
#
#
# def AndroidDeviceByMongoDBID(mongoDBId):
#     return "enterprise/rest/v3/device/android/{mongoDBId}".format(mongoDBId=mongoDBId)
#
#
# FCMUpdate = "enterprise/rest/weguard-v2/fcmUpdate"
#
#
# def AndroidNotes(androidDeviceID, page, limit):
#     return "enterprise/rest/notes/{androidDeviceID}?page={page}&limit={limit}".format(androidDeviceID=androidDeviceID,
#                                                                                       page=page, limit=limit)
#
#
# def AndroidActivity(page, size):
#     allLogs = "enterprise/rest/weguard/logs/eventsPerAccount?page={page}&size={size}".format(page=page, size=size)
#     return allLogs
#
#
# def ScreenShareHistory(AndroidDeviceID, page, size, email):
#     return ("enterprise/rest/webrtc/screensharehistory/{AndroidDeviceID}?"
#             "page={page}&pageSize={size}&email={email}").format(
#         AndroidDeviceID=AndroidDeviceID, page=page, size=size, email=email)
#
#
# def AndroidDeviceApps(AndroidDeviceID):
#     return "enterprise/rest/deviceapps/apps/{AndroidDeviceID}".format(AndroidDeviceID=AndroidDeviceID)
#
#
# def AndroidDeviceBroadcastHistory(AndroidDeviceID, page, pageSize):
#     return "enterprise/rest/broadcast/history/device/{AndroidDeviceID}?pageNo={page}&pageSize={pageSize}&type=FCM_MESSAGE".format(
#         AndroidDeviceID=AndroidDeviceID, page=page, pageSize=pageSize)
#
#
# AndroidDeviceLastContactTime = "enterprise/rest/v3/device/last-contact-time"
#
#
# def AndroidDeviceDataUsage(AndroidDeviceID):
#     return "enterprise/rest/app/device/{AndroidDeviceID}".format(AndroidDeviceID=AndroidDeviceID)
#
#
# def AndroidDeviceEnterpriseAppSizes(AndroidDeviceID, AndroidDeviceMongoDBID):
#     return "enterprise/rest/apkdownload/{AndroidDeviceID}/{AndroidDeviceMongoDBID}".format(
#         AndroidDeviceID=AndroidDeviceID, AndroidDeviceMongoDBID=AndroidDeviceMongoDBID)
#
#
# # GET -- Clicking on Android Device ID (get details by policyID)
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5001_GET_Android_Device_By_PolicyID == 0,
#                     reason="GET Android Device by MongoDB ID is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50001)
# def test_tc_5001_Android_Device_By_PolicyID_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policy_id in globalvar.Android_Policy_IDs:
#             apiUrl = globalvar.BaseURL + AndroidDeviceByPolicyID(policy_id)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device by policy ID) ---------------------------\n\n")
#         assert False
#
#
# # GET -- Clicking on Android Device ID (get details by Mongo DB ID)
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5002_GET_Android_Device_By_MongoDBID == 0,
#                     reason="GET Android Device by MongoDB ID is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50002)
# def test_tc_5002_Android_Device_By_MongoDBID_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for mongoDBID in globalvar.Android_Mongo_DB_DeviceIDs:
#             apiUrl = globalvar.BaseURL + AndroidDeviceByMongoDBID(mongoDBID)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device by MongoDB ID ---------------------------\n\n")
#         assert False
#
#
# # POST -- FCM Update of APK DU
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5003_POST_Android_Device_FCMUpdate_DU == 0, reason="FCM Update APK DU is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50003)
# def test_tc_5003_Android_Device_APK_DU_FCMUpdate(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for Android_DeviceID in globalvar.Android_DeviceIDs:
#             for policyID in globalvar.Android_Policy_IDs:
#                 apiUrl = globalvar.BaseURL + FCMUpdate
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#                 APKDUPayload = {
#                     "topic": Android_DeviceID + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
#                     "type": "FCM_APK_DU", "isLicenseLevel": False,
#                     "pId": policyID, "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode,
#                     "priority": "high"}
#                 res = requests.post(url=apiUrl, headers=Headers, json=APKDUPayload, timeout=globalvar.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print(#"\n" + "Header: " + str(res.headers) + "\n"
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Request Payload: " + str(APKDUPayload) +
#                           "\n" + "Response: " + str(res.content) + "\n")
#                 elif res.status_code == 400:
#                     print("\n" + "400 Bad Request!" + "\n")
#                     # Add your assertions or actions for 400 Bad Request response here
#                     assert False, "Received 400 Bad Request response"
#                 elif res.status_code == 404:
#                     print("\n" + "404 Result not found!" + "\n")
#                     # Add your assertions or actions for 404 Not Found response here
#                     assert False, "Received 404 response"
#                 elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!" + "\n")
#                     # Add your assertions or actions for 500 Internal Server Error response here
#                     assert False, "Received 500 response"
#                 else:
#                     print("Request did not succeed! Status code:", res.status_code)
#                     assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to FCM Update for APK DU ---------------------------\n\n")
#         assert False
#
#
# # GET -- Get Notes for Android Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5004_GET_Android_Device_Notes == 0,
#                     reason="GET Android Device Notes is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50004)
# def test_tc_5004_Android_Device_Notes_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             apiUrl = globalvar.BaseURL + AndroidNotes(AndroidDeviceID, globalvar.page_1, globalvar.page_500)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Notes ---------------------------\n\n")
#         assert False
#
#
# # GET Android Activity Logs
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5005_POST_Android_Device_Activity == 0,
#                     reason="Android Device Logs in device details view is skipped")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.devicedetailsview
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50005)
# def test_tc_5005_Android_Device_Logs(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for android_device_id in globalvar.Android_DeviceIDs:
#             print(f"Processing Android devices: {android_device_id}")
#             apiUrl = globalvar.BaseURL + AndroidActivity(globalvar.page_1, globalvar.page_1000)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             Android_payload = {
#                 "startDate": globalvar.start_timestamp,
#                 "endDate": globalvar.end_timestamp,
#                 "event": "All",
#                 "logLevel": "All",
#                 "deviceIds": [android_device_id],
#                 "policyIds": None
#             }
#             print(Android_payload)
#             res = requests.post(url=apiUrl, headers=Headers, json=Android_payload, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#                 # Print information about the current test case
#                 print(f" Android Device logs are fetched" + "\n")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Request Payload: " + str(Android_payload) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(f"Android Device logs are not fetched" + "\n")
#         assert False
#
#
# # GET -- Get Screen Share History of Android Device
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5006_GET_Android_Device_ScreenShareHistory == 0,
#                     reason="GET Android Device Screen Share History is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50006)
# def test_tc_5006_Android_Device_Notes_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             apiUrl = globalvar.BaseURL + ScreenShareHistory(AndroidDeviceID, globalvar.page_1, globalvar.page_500,
#                                                             globalvar.userName)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Screen Share History ---------------------------\n\n")
#         assert False
#
#
# # GET -- Android Device Apps
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5007_GET_Android_Device_Apps == 0,
#                     reason="GET Android Device Apps is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50007)
# def test_tc_5007_Android_Device_Apps_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             apiUrl = globalvar.BaseURL + AndroidDeviceApps(AndroidDeviceID)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Apps ---------------------------\n\n")
#         assert False
#
#
# # GET -- Android Device Broadcast History
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5008_GET_Android_Device_Broadcast_History == 0,
#                     reason="GET Android Device Broadcast History is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50008)
# def test_tc_5008_Android_Device_Broadcast_History_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             apiUrl = globalvar.BaseURL + AndroidDeviceBroadcastHistory(AndroidDeviceID, globalvar.page_1,
#                                                                        globalvar.page_500)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Broadcast History ---------------------------\n\n")
#         assert False
#
#
# # PUT -- Android Device Last Contact Time
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5009_PUT_Android_Device_Last_Contact_Time == 0,
#                     reason="PUT Android Device Last Contact Time is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50009)
# def test_tc_5009_Android_Device_Last_Contact_Time_PUT(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             apiUrl = globalvar.BaseURL + AndroidDeviceLastContactTime
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             LastContactTimeAndroidPayload = {"deviceId": AndroidDeviceID, "lastContactTime": globalvar.isostart}
#             res = requests.put(url=apiUrl, headers=Headers, json=LastContactTimeAndroidPayload,
#                                timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Request Payload: " + str(LastContactTimeAndroidPayload) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Last Contact Time ---------------------------\n\n")
#         assert False
#
#
# # GET -- Android Device Broadcast History
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5010_GET_Android_Device_Data_Usage == 0,
#                     reason="GET Android Device Data Usage is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50010)
# def test_tc_5010_Android_Device_Data_Usage_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             apiUrl = globalvar.BaseURL + AndroidDeviceDataUsage(AndroidDeviceID)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Data Usage ---------------------------\n\n")
#         assert False
#
#
# # GET -- Android Device Broadcast History
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5011_GET_Android_Device_Enterprise_AppSizes == 0,
#                     reason="GET Android Device Enterprise App Sizes is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50011)
# def test_tc_5011_Android_Device_Enterprise_AppSizes_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for AndroidDeviceID in globalvar.Android_DeviceIDs:
#             for AndroidDeviceMongoID in globalvar.Android_Mongo_DB_DeviceIDs:
#                 apiUrl = globalvar.BaseURL + AndroidDeviceEnterpriseAppSizes(AndroidDeviceID, AndroidDeviceMongoID)
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#                 res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print(#"\n" + "Header: " + str(res.headers) + "\n"
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Response: " + str(res.content) + "\n")
#                 elif res.status_code == 400:
#                     print("\n" + "400 Bad Request!" + "\n")
#                     # Add your assertions or actions for 400 Bad Request response here
#                     assert False, "Received 400 Bad Request response"
#                 elif res.status_code == 404:
#                     print("\n" + "404 Result not found!" + "\n")
#                     # Add your assertions or actions for 404 Not Found response here
#                     assert False, "Received 404 response"
#                 elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!" + "\n")
#                     # Add your assertions or actions for 500 Internal Server Error response here
#                     assert False, "Received 500 response"
#                 else:
#                     print("Request did not succeed! Status code:", res.status_code)
#                     assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the Android Device Enterprise App Sizes ---------------------------\n\n")
#         assert False
#
#
# # POST -- FCM Update of Device Wake Up
# # When device is Offline and clicking on device id
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_5012_POST_Android_Device_Wake_Up == 0,
#                     reason="FCM Update Device Wake Up is skipped")
# @pytest.mark.positivetest
# @pytest.mark.devicedetailsview
# @pytest.mark.regressiontest
# @pytest.mark.run(order=50012)
# def test_tc_5012_Android_Device_Wake_Up_FCMUpdate(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for Android_DeviceID in globalvar.Android_DeviceIDs:
#             for policyID in globalvar.Android_Policy_IDs:
#                 apiUrl = globalvar.BaseURL + FCMUpdate
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#                 DeviceWakeUpPayload = {
#                     "topic": Android_DeviceID + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
#                     "type": "DEVICE_WAKEUP", "priority": "high", "isLicenseLevel": False,
#                     "pId": policyID, "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode, }
#                 res = requests.post(url=apiUrl, headers=Headers, json=DeviceWakeUpPayload, timeout=globalvar.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print(#"\n" + "Header: " + str(res.headers) + "\n"
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Request Payload: " + str(DeviceWakeUpPayload) +
#                           "\n" + "Response: " + str(res.content) + "\n")
#                 elif res.status_code == 400:
#                     print("\n" + "400 Bad Request!" + "\n")
#                     # Add your assertions or actions for 400 Bad Request response here
#                     assert False, "Received 400 Bad Request response"
#                 elif res.status_code == 404:
#                     print("\n" + "404 Result not found!" + "\n")
#                     # Add your assertions or actions for 404 Not Found response here
#                     assert False, "Received 404 response"
#                 elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!" + "\n")
#                     # Add your assertions or actions for 500 Internal Server Error response here
#                     assert False, "Received 500 response"
#                 else:
#                     print("Request did not succeed! Status code:", res.status_code)
#                     assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to FCM Update for Device Wake Up ---------------------------\n\n")
#         assert False
