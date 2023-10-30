# import json
# from datetime import datetime
# import pytest
# import requests
# import globalvariables as globalvar
# import Executor as Execute
# import test_GETutils as Utils
# import general_payload as GeneralPayload
#
# CloneWindowsPolicy = "windows/rest/policy"
#
#
# def DeleteWindowsPolicy(policyId):
#     return "windows/rest/policy/{policyId}".format(policyId=policyId)
#
#
# def GETPolicyByMongoID(policyMongoID):
#     return "windows/rest/policy/{policyMongoID}".format(policyMongoID=policyMongoID)
#
#
# def GETDisabledAppsWindows(policyId):
#     return "windows/rest/disableapp/policy/{policyId}".format(policyId=policyId)
#
#
# def WindowsDevicePolicy(policyId, size, page):
#     return "windows/rest/device/policy/{policyId}?size={size}&page={page}".format(policyId=policyId, size=size,
#                                                                                   page=page)
#
#
# def WindowsPolicyUpdate(policyId):
#     return "windows/rest/policy/{policyId}".format(policyId=policyId)
#
#
# # GET method to get the Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100001_Windows_Policy_GET == 0, reason="GET Windows Policy is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsPolicy
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100001)
# def test_tc_1100001_Windows_Policy_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyID in globalvar.Windows_Policy_IDs:
#             apiUrl = globalvar.BaseURL + GETPolicyByMongoID(policyID)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#                 globalvar.PolicyWindowsID = json.loads(res.content)['entity']['id']
#                 print("\n" + "ID from GET Policy API: ", globalvar.PolicyWindowsID)
#                 globalvar.PolicyWindowsVersion = json.loads(res.content)['entity']['version']
#                 print("\n" + "Policy version from GET Policy API: ", globalvar.PolicyWindowsVersion, "\n")
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
#             "------------- Failed to display the Windows policy ---------------------------\n\n")
#         assert False
#
#
# # POST method to clone a Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100002_Windows_Policy_Clone_POST == 0, reason="Windows Policy Clone is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsPolicy
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100002)
# def test_tc_1100002_Windows_Policy_Clone_POST(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         if globalvar.Windows_Policy_IDs and globalvar.Windows_Policy_Types:
#             policy_id = globalvar.Windows_Policy_IDs[0]  # Take the first policy ID from the list
#             policyType = globalvar.Windows_Policy_Types[0]  # Take the first policy type from the list
#             WindowsDevices = CloneWindowsPolicy
#             apiUrl = globalvar.BaseURL + WindowsDevices
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             # Generate a unique display name by appending a timestamp
#             unique_groupDisplayName = f"{GeneralPayload.firstName}_{int(datetime.now().timestamp())}"
#             Payload = {"clonedFrom": policy_id, "clonedFromName": policy_id,
#                        "description": GeneralPayload.randomName,
#                        "groupDisplayName": unique_groupDisplayName, "type": policyType}
#             res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Request Payload: " + str(Payload) +
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
#         else:
#             print("Empty policy ID list or policy type list.")
#             pytest.skip("No policy data available.")
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to clone the Windows policy ---------------------------\n\n")
#         assert False
#
#
# # Delete method to delete the Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100003_Windows_Policy_Delete == 0, reason="Delete Windows Policy is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsPolicy
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100003)
# def test_tc_1100003_Windows_Policy_DELETE(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         # for policyId in globalvar.Windows_Policy_IDs:
#         policyId = globalvar.Windows_Policy_IDs[0]
#         apiUrl = globalvar.BaseURL + DeleteWindowsPolicy(policyId)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.delete(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n200 The request was a success!")
#             print("\nRequest URL: " + apiUrl +
#                   "\nRequest Method: " + res.request.method +
#                   "\nStatus Code: " + str(res.status_code) +
#                   "\nResponse: " + str(res.content) + "\n")
#         elif res.status_code == 204:  # Assuming a successful deletion returns 204
#             print("\n204 No Content. The request was a success!")
#         elif res.status_code == 400:
#             print("\n400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n500 Internal Server Error!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to delete the Windows policy ---------------------------\n\n")
#         assert False
#
#
# # GET method to get the Windows Disabled Apps in the policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100004_Windows_Disabled_Apps_GET == 0, reason="Windows Disabled Apps is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsPolicy
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100004)
# def test_tc_1100004_Windows_DisabledApps_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyID in globalvar.Windows_Policy_IDs:
#             apiUrl = globalvar.BaseURL + GETDisabledAppsWindows(policyID)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to display the Windows disabled apps in policy ---------------------------\n\n")
#         assert False
#
#
# # GET method to get the Windows Device policy
# @pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
# @pytest.mark.skipif(Execute.test_tc_1100005_Windows_Device_Policy_GET == 0, reason="Windows Device Policy is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsPolicy
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100005)
# def test_tc_1100005_Windows_DevicePolicy_GET(Page, Size):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyID in globalvar.Windows_Policy_IDs:
#             apiUrl = globalvar.BaseURL + WindowsDevicePolicy(policyID, Size, Page)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
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
#             "------------- Failed to display the Windows device policy ---------------------------\n\n")
#         assert False
#
#
# # PUT method to update the Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100006_Windows_Policy_Update_PUT == 0,
#                     reason="PUT - Windows Policy Update is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsPolicy
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100006)
# def test_tc_1100006_Windows_PolicyUpdate_PUT(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         # for policyID in globalvar.Windows_Policy_IDs:
#         policyId = globalvar.Windows_Policy_IDs[0]
#         apiUrl = globalvar.BaseURL + WindowsPolicyUpdate(policyId)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.put(url=apiUrl, headers=Headers, json=GeneralPayload.WindowsPolicyUpdate,
#                            timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print("\n" + "200 The request was a success!")
#             print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                 "\n" + "Request URL: " + apiUrl +
#                 "\n" + "Request Method: " + res.request.method +
#                 "\n" + "Status Code: " + str(res.status_code) +
#                 "\n" + "Response: " + str(res.content) + "\n")
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
#         print("------------- Failed to display the Windows device policy ---------------------------\n\n")
#         assert False
