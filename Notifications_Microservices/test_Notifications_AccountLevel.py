# import datetime
# import json
#
# import pytest
# import requests
#
# import Executor as Execute
# import WeGuardlogger as WeGuard
# import globalvariables
# import general_payload as Payload
# import test_GETutils as Utils
#
#
# def url_formatter1(accountId):
#     GETAccountLevelNotifications = "notification/rest/notification/all/account/{accountId}".format(accountId=accountId)
#     return GETAccountLevelNotifications
#
#
# def url_formatter2(alertid):
#     PUTAccountLevelNotifications = "notification/rest/notification/all/account/{alertid}".format(alertid=alertid)
#     return PUTAccountLevelNotifications
#
#
# # GET method to get all the Account Level Notifications
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_000010_Notifications_AccountLevel_GET == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10005)
# def test_tc_000005_GET_AccountLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         GetAccountLevelNotifications = url_formatter1(globalvariables.accountId)
#         apiUrl = globalvariables.BaseURL + GetAccountLevelNotifications
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         #        print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             globalvariables.accountId = json.loads(res.content)['entities'][0]['accountId']
#             print(globalvariables.accountId)
#             globalvariables.getAlertId = json.loads(res.content)['entities'][0]['id']
#             print(globalvariables.getAlertId)
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
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
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # PUT method to update Account Level Notifications with Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_000012_Notifications_AccountLevel_PUT == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10007)
# def test_tc_000007_PUT_AccountLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#
#     try:
#         PUTAccountLevelNotifications = url_formatter2(globalvariables.getAlertId)
#         apiUrl = globalvariables.BaseURL + PUTAccountLevelNotifications
#         headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.put(url=apiUrl, headers=headers, json=Payload.PutAccountLevelNotifications,
#                            timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
#         else:
#             if res.status_code == 400:
#                 print("\n" + "400 Bad Request!")
#             elif res.status_code == 404:
#                 print("\n" + "500 Result not found!")
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!")
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         WeGuard.logger.error("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
