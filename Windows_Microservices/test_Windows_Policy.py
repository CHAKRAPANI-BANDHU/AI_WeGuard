#
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
# def DeleteWindowsPolicy(policyId):
#     return "windows/rest/policy/{policyId}".format(policyId=policyId)
#
# def GETPolicyByMongoID(policyMongoID):
#     return "windows/rest/policy/{policyMongoID}".format(policyMongoID=policyMongoID)
#
# # POST method to clone a Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100001_Windows_Policy_Clone_POST == 0, reason="skip test")
# @pytest.mark.positivetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100001)
# def test_tc_1100001_Windows_Policy_Clone_POST(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policy_id in globalvar.Windows_Policy_IDs:
#             for policyType in globalvar.Windows_Policy_Types:
#                 WindowsDevices = CloneWindowsPolicy
#                 apiUrl = globalvar.BaseURL + WindowsDevices
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#                 # Generate a unique display name by appending a timestamp
#                 unique_groupDisplayName = f"{GeneralPayload.firstName}_{int(datetime.now().timestamp())}"
#                 Payload = {"clonedFrom": policy_id, "clonedFromName": policy_id,
#                            "description": GeneralPayload.randomName,
#                            "groupDisplayName": unique_groupDisplayName, "type": policyType}
#                 res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
#                 if res.status_code == 200:
#                     curl_str1 = Utils.getCurlEquivalent(res)
#                     print(curl_str1)
#                     print("\n" + "200 The request was a success!")
#                     print("\n" + "Header: " + str(res.headers) +
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Request Payload: " + str(Payload),
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
#             "------------- Failed to clone the Windows policy ---------------------------\n\n")
#         assert False
#
# # Delete method to delete the Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100002_Windows_Policy_Delete == 0, reason="skip test")
# @pytest.mark.positivetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100002)
# def test_tc_1100002_Windows_Policy_DELETE(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policy_id in globalvar.Windows_Policy_IDs:
#             apiUrl = globalvar.BaseURL + DeleteWindowsPolicy(policy_id)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.delete(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
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
#             "------------- Failed to delete the Windows policy ---------------------------\n\n")
#         assert False
#
# # Delete method to delete the Windows policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1100003_Windows_Policy_GET == 0, reason="skip test")
# @pytest.mark.positivetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1100003)
# def test_tc_1100003_Windows_Policy_GET(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyMongoID in globalvar.Wind:
#             apiUrl = globalvar.BaseURL + DeleteWindowsPolicy(policyMongoID)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
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
#             "------------- Failed to display the Windows policy ---------------------------\n\n")
#         assert False
