# import datetime
#
# import pytest
# import requests
#
# import Executor as Execute
# import WeGuardlogger as WeGuard
# import globalvariables
# import general_payload as Details
# import test_GETutils as Utils
#
# POSTAccountLevelNotifications = "notification/rest/notification"
#
#
# def url_formatter2(alertid):
#     PUTNotifications = "notification/rest/notification/{alertid}".format(alertid=alertid)
#     return PUTNotifications
#
#
# # POST method to get all the Account Level Notifications without Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_000011_Notifications_AccountLevel_POST == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10006)
# def test_tc_000006_POST_AccountLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         apiUrl = globalvariables.BaseURL + POSTAccountLevelNotifications
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=Details.PostAccountLevelAlertConfig,
#                             timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
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
# # POST method to get all the Account Level Notifications without Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_000020_Notifications_PolicyLevel_POST == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=100021)
# def test_tc_000008_POST_PolicyLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         apiUrl = globalvariables.BaseURL + POSTAccountLevelNotifications
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=Details.PostPolicyLevelAlertConfig,
#                             timeout=globalvariables.timeout)
#         Details.PostPolicyLevelAlertConfig["policyId"] = globalvariables.Android_profile_ids
#         Details.PostPolicyLevelAlertConfig["accountId"] = globalvariables.accountId
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
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
# @pytest.mark.skipif(Execute.test_000016_Notifications_PUT == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10022)
# def test_tc_000007_PUT_Notifications_Update(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         Notifications = url_formatter2(globalvariables.getAlertId)
#         apiUrl = globalvariables.BaseURL + Notifications
#         headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.put(url=apiUrl, headers=headers, json=Details.Notifications,
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
