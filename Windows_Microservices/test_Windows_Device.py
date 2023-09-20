# from datetime import datetime
# import pytest
# import requests
# import globalvariables
# import globalvariables as globalvar
# import Executor as Execute
# import test_GETutils as Utils
# import general_payload as GeneralPayload
#
#
# def WindowsDevice(WindowsMongoDBID):
#     return "windows/rest/device/{WindowsMongoDBID}".format(WindowsMongoDBID=WindowsMongoDBID)
#
#
# def WindowsDeviceDetails(end, page, policyId, size, start):
#     return "windows/rest/device/all?end={end}&page={page}&policyId={policyId}&size={size}&start={start}".format(end=end, page=page, policyId=policyId, size=size, start=start)
#
# def WindowsDevicesByPolicyIDs(page, size):
#     return "windows/rest/device/bulk?page={page}&size={size}".format(page=page, size=size)
#
# def WindowsDeviceCommand(WindowsMongoDBID):
#     return "windows/rest/device/command/{WindowsMongoDBID}".format(WindowsMongoDBID=WindowsMongoDBID)
#
# LastConactTime = "windows/rest/device/last-contactime"
#
# def WindowsDeviceDetailsByPolicyID(policyId, page, size):
#     return "windows/rest/device/policy/{policyId}?page={page}&size={size}".format(policyId=policyId, page=page, size=size)
#
# def SearchWindowsDeviceByPolicyID(policyId, page, size):
#     return "windows/rest/device/search/{policyId}?page={page}&size={size}".format(policyId=policyId, page=page, size=size)
#
# def SearchStringWindowsDevice(page, searchString, size):
#     return "windows/rest/device/search/all?page={page}&searchString={searchString}&size={size}".format(page=page, searchString=searchString, size=size)
#
#
# # GET method to get Windows devices by Mongo DB ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000001_Windows_DeviceDetailsByMongoID_GET == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100001)
# def test_tc_0000001_Windows_Device_Details_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
#             WindowsDevices = WindowsDevice(mongodbId)
#             apiUrl = globalvar.BaseURL + WindowsDevices
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to display the Windows device details by Mongo DB ID ---------------------------\n\n")
#         assert False
#
#
# # PUT method to update the tags for Windows devices by Mongo DB ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000002_Windows_Device_Updates_Tags_By_MongoID_PUT == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100002)
# def test_tc_0000002_Windows_Device_Updates_Tags_By_MongoID_PUT(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
#             WindowsDevices = WindowsDevice(mongodbId)
#             apiUrl = globalvar.BaseURL + WindowsDevices
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.put(url=apiUrl, headers=Headers, json=GeneralPayload.PUT_UpdateTags_Windows_Device,
#                                timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to update the tags for the Windows devices by Mongo DB ID ---------------------------\n\n")
#         assert False
#
#
# # GET method to fetch device details by policy id
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000003_Windows_Fetch_Device_Details_GET == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100003)
# def test_tc_0000003_Windows_Fetch_Device_Details_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policy_id in globalvar.Windows_Policy_IDs:
#             WindowsDevices = WindowsDeviceDetails(globalvar.isoend, globalvar.page_1, policy_id, globalvar.page_1000,
#                                                   globalvar.isostart)
#             apiUrl = globalvar.BaseURL + WindowsDevices
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to fetch Windows device details by policy id ---------------------------\n\n")
#         assert False
#
#
# # POST method to fetch devices by PolicyIds
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000004_Windows_Fetch_Devices_By_PolicyIDs_POST == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100004)
# def test_tc_0000004_Windows_Fetch_Devices_By_PolicyIDs_POST(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policy_id in globalvar.Windows_Policy_IDs:
#             WindowsDevices = WindowsDevicesByPolicyIDs(globalvar.page_1, globalvar.page_1000)
#             apiUrl = globalvar.BaseURL + WindowsDevices
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             Payload = {"policyIds": [policy_id]}
#             res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to fetch Windows device details by policy id ---------------------------\n\n")
#         assert False
#
#
# # POST method to add commands
# # Restart of a device
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000005_Windows_Add_Device_Commands_POST == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100005)
# def test_tc_0000005_POST_Windows_Add_Device_Commands(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
#             apiUrl = globalvar.BaseURL + WindowsDeviceCommand(mongodbId)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             Payload = {"command": "RebootNow"}
#             # For Wipe: RemoteWipe & type
#             res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to execute the device command ---------------------------\n\n")
#         assert False
#
#
# # PUT method to verify the last contact time of the Windows devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000006_Windows_Device_Last_Contact_Time_PUT == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100006)
# def test_tc_0000006_Windows_PUT_Device_Last_Contact_Time(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for DeviceId in globalvar.Windows_DeviceIDs:
#             apiUrl = globalvar.BaseURL + LastConactTime
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             ContactTime = {"deviceId": DeviceId, "lastContactTime": globalvariables.isocurrent}
#             res = requests.put(url=apiUrl, headers=Headers, json=ContactTime, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to update the last contact time for the Windows device ---------------------------\n\n")
#         assert False
#
#
# # GET method to get the Windows device details by policyId
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000007_Windows_DeviceDetailsByPolicyID_GET == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100007)
# def test_tc_0000007_Windows_GET_Device_Details_By_PolicyID(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#       for policy_id in globalvar.Windows_Policy_IDs:
#         apiUrl = globalvar.BaseURL + WindowsDeviceDetailsByPolicyID(policy_id, globalvariables.page_1, globalvariables.page_500)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print("\n" + "200 The request was a success!")
#             print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- GET Failed to get the Windows device details by policyId ---------------------------\n\n")
#         assert False
#
# # GET method to search the Windows device by policyId
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000008_Windows_Device_Search_By_PolicyID_GET == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100008)
# def test_tc_0000008_Windows_GET_Device_Search_By_PolicyID(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#       for policy_id in globalvar.Windows_Policy_IDs:
#         apiUrl = globalvar.BaseURL + SearchWindowsDeviceByPolicyID(policy_id, globalvariables.page_1, globalvariables.page_500)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print("\n" + "200 The request was a success!")
#             print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- GET Failed to get the Windows device by policyId ---------------------------\n\n")
#         assert False
#
# # GET method to search the Windows device by all string/complete deviceId
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_0000009_Windows_Device_Search_By_All_String_GET == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100009)
# def test_tc_0000009_Windows_GET_Search_Device_By_All_String(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#       for DeviceId in globalvar.Windows_DeviceIDs:
#         apiUrl = globalvar.BaseURL + SearchStringWindowsDevice(globalvariables.page_1, DeviceId, globalvariables.page_500)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print("\n" + "200 The request was a success!")
#             print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- GET Failed to search the Windows device by all string/complete deviceId ---------------------------\n\n")
#         assert False
