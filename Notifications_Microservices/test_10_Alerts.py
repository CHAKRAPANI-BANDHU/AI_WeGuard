# import json
# from datetime import datetime
# import pytest
# import requests
# import Executor as Execute
# import globalvariables
# import test_GETutils as Utils
#
#
# def AlertTypes(accountId, start, end, page, size, type):
#     url5 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, type=type)
#     return url5
#
#
# def AlertLevels(accountId, start, end, page, size, level):
#     url6 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&level={level}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, level=level)
#     return url6
#
#
# def AlertTypeLevels(accountId, start, end, page, size, type, level):
#     url4 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}&level={level}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, type=type, level=level)
#     return url4
#
#
# def AllAlerts(accountId, start, end, page, size):
#     GETAccountLevelAlert = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size)
#     return GETAccountLevelAlert
#
#
# def UnacknowledgedAlerts(accountId, start, end, page, size, level, ack):
#     url6 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&level={level}&ack={ack}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, level=level, ack=ack)
#     return url6
#
#
# def AcknowledgedAlerts(accountId):
#     AcknowledgeAlerts = "notification/rest/alert/account/{accountId}/read".format(accountId=accountId)
#     return AcknowledgeAlerts
#
#
# # Define the list of alert types
# Alert_Types = ["ALL", "BATTERY", "DATA_USAGE", "KIOSK_LOCKED", "KIOSK_UNLOCKED", "ADMIN_LOCKED", "DEVICE_REBOOTED",
#                "DEVICE_SHUTDOWN", "DEVICE_WIPED", "DEVICE_DELETED", "ROOTED_ENROLL", "MEMORY_ALERT", "DISC_USAGE",
#                "DEVICE_MARKED_REPLACED", "DEVICE_MARKED_LOST", "DEVICE_MARKED_STOLEN", "DEVICE_CONNECTED_BACK",
#                "SIM_LOCK_CHANGED", "RESET_PASSWORD", "SIM_REMOVED", "SIM_CHANGED", "SIM_ADDED", "UNINSTALL_WEGUARD"]
#
# # Define the list of alert level
# Alert_Levels = ["ALL", "LOW", "WARNING", "CRITICAL", "IN_FENCE", "OUT_FENCE"]
#
#
# # Alert Types
# @pytest.mark.parametrize('alert_type', Alert_Types)
# @pytest.mark.skipif(Execute.test_tc_1001_Alerts_Types_and_Levels_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10431)
# def test_Alert_Types(alert_type):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         alert_url = AlertTypes(globalvariables.accountId, globalvariables.isostart, globalvariables.isoend,
#                                globalvariables.page_1, globalvariables.page_1000, alert_type)
#         apiUrl = globalvariables.BaseURL + alert_url
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content))
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
#             assert False, f"Received {res.status_code} response"
#         print(
#             f"\n------------------- Alert notifications of type={alert_type} and level=All ---------------------------\n")
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             f"\n------------------- Not available alert notifications of type={alert_type} and level=All ---------------------------\n")
#         assert False
#
#
# # Alert Levels
# @pytest.mark.parametrize('alert_level', Alert_Levels)
# @pytest.mark.skipif(Execute.test_tc_1002_Alerts_Levels == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10432)
# def test_Alert_Levels(alert_level):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         alert_level = AlertLevels(globalvariables.accountId, globalvariables.isostart, globalvariables.isoend,
#                                   globalvariables.page_1, globalvariables.page_1000, alert_level)
#         apiUrl = globalvariables.BaseURL + alert_level
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content))
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
#             assert False, f"Received {res.status_code} response"
#         print(
#             f"\n------------------- Alert notifications of type={alert_level} and level=All ---------------------------\n")
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             f"\n------------------- Not available alert notifications of type={alert_level} and level=All ---------------------------\n")
#         assert False
#
#
# # Fixture to check if test_tc_1003_Alerts_Types_and_Levels is set to 1
# @pytest.fixture
# def check_test_tc_1003_Alerts_Types_and_Levels():
#     return Execute.test_tc_1003_Alerts_Types_and_Levels == 1
#
# # Alert Types and Levels
# @pytest.mark.parametrize('alert_type, alert_level', [(alert_type, alert_level) for alert_type in Alert_Types for alert_level in Alert_Levels])
# @pytest.mark.skipif(not check_test_tc_1003_Alerts_Types_and_Levels,
#                     reason="This test must run, it is mandatory. Without this test, rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10433)
# def test_AlertTypes_and_AlertLevels(alert_type, alert_level):
#     now1 = datetime.now()
#     try:
#         apiUrl = globalvariables.BaseURL + AlertTypeLevels(globalvariables.accountId, globalvariables.isostart,
#                                     globalvariables.isoend, globalvariables.page_1,
#                                     globalvariables.page_1000,
#                                     alert_type, alert_level)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print(f"------------------- Filter By Alert type={alert_type} and level={alert_level} ---------------------------\n")
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!" + "\n")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content))
#         elif res.status_code == 400:
#             print("\n400 Bad Request!")
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n404 Result not found!")
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n500 Internal Server Error!")
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code: " + str(res.status_code))
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(f"------------------- Failed to display the Filter By Alert type={alert_type} and level={alert_level} ---------------------------\n")
#         assert False
#
#
#
# # GET method to get critical alerts that are not acknowledged by user after clicking on Alert notification icon
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1004_Unacknowledged_Alerts_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10444)
# def test_Unacknowledged_Critical_Alerts(url):
#     level = 'CRITICAL'
#     ack = 'unread'
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         UnacknowledgedCriticalAlerts = UnacknowledgedAlerts(globalvariables.accountId, globalvariables.isomonth,
#                                                             globalvariables.isoend, globalvariables.page_1,
#                                                             globalvariables.page_100, level, ack)
#         apiUrl = globalvariables.BaseURL + UnacknowledgedCriticalAlerts
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             response_data = json.loads(res.content)
#             # Access the 'list' key within the 'entity' dictionary
#             AlertIDs_lists = response_data['entity']['list']
#             # Iterate through each item in the list
#             for alertIds in AlertIDs_lists:
#                 # Check if the alert is unacknowledged (assuming 'read' indicates acknowledgement)
#                 if not alertIds['read']:
#                     # Access the 'id' field from the current item
#                     item_id = alertIds['id']
#                     # Append the unacknowledged alert ID to the array
#                     globalvariables.UnacknowledgeAlertsIDs.append(item_id)
#             print("\n200 The request was a success!\n")
#             print(
#                 "\n------------------- Displaying Unacknowledged Critical Alerts all alert types and levels ---------------------------\n")
#             print("\nHeader: " + str(res.headers) +
#                   "\nRequest URL: " + apiUrl +
#                   "\nRequest Method: " + res.request.method +
#                   "\nStatus Code: " + str(res.status_code) +
#                   "\nResponse: " + str(res.content) + "\n")
#         else:
#             print(f"Request did not succeed! Status code: {res.status_code}")
#             if res.status_code == 400:
#                 print("400 Bad Request!")
#             elif res.status_code == 404:
#                 print("404 Result not found!")
#             elif res.status_code == 500:
#                 print("500 Internal Server Error!")
#                 # Add your assertions or actions for different response codes here
#                 assert False, f"Received {res.status_code} response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n------------------- Not displaying Unacknowledged Critical Alerts all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to get critical alerts that are acknowledged by user after clicking on Alert notification icon
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1005_Acknowledge_Alerts_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10445)
# def test_Acknowledged_Critical_Alerts(url):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         AcknowledgedCriticalAlerts = AcknowledgedAlerts(globalvariables.accountId)
#         apiUrl = globalvariables.BaseURL + AcknowledgedCriticalAlerts
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         for alert_id in globalvariables.UnacknowledgeAlertsIDs:
#             payload = [alert_id]
#             res = requests.put(url=apiUrl, headers=Headers, json=payload,
#                                timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print("\n------------------- Acknowledged Critical Alerts ---------------------------\n")
#             else:
#                 if res.status_code == 400:
#                     print("\n" + "400 Bad Request!" + "\n")
#                 elif res.status_code == 404:
#                     print("\n" + "404 Result not found!" + "\n")
#                 elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!" + "\n")
#                 else:
#                     print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n------------------- Unacknowledged critical alerts  ---------------------------\n")
#         assert False
#
#
# # GET method to GET all level and types alert notifications of Today's
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1006_TodaysAlerts == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10446)
# def test_TodaysAlertsTypesLevelAll(url):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         TodaysAlertsTypesLevelAll = AllAlerts(globalvariables.accountId, globalvariables.isostart,
#                                               globalvariables.isoend, globalvariables.page_1,
#                                               globalvariables.page_100)
#         apiUrl = globalvariables.BaseURL + TodaysAlertsTypesLevelAll
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#             print("\n------------------- Displaying Todays all alert types and levels ---------------------------\n")
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
#         print("\n------------------- Not displaying all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to GET all level and types alert notifications of Yesterday's
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1007_YesterdaysAlerts == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10447)
# def test_YesterdaysAlertsTypesLevelAll(url):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         AlertsTypesLevelAllYesterday = AllAlerts(globalvariables.accountId, globalvariables.isocustom,
#                                                  globalvariables.isoyesterday,
#                                                  globalvariables.page_1, globalvariables.page_100)
#         apiUrl = globalvariables.BaseURL + AlertsTypesLevelAllYesterday
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#             print(
#                 "\n------------------- Displaying Yesterday's all alert types and levels ---------------------------\n")
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
#             "\n------------------- Yesterday's -- Not displaying all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to GET all level and types alert notifications of Custom Date Range
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1008_CustomDateRange == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10448)
# def test_CustomDateRangeAlertsTypesLevelAll(url):
#     now1 = datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         AlertsTypesLevelAllCustomDateRange = AllAlerts(globalvariables.accountId, globalvariables.iso1weekcustom,
#                                                        globalvariables.isoend,
#                                                        globalvariables.page_1, globalvariables.page_100)
#         apiUrl = globalvariables.BaseURL + AlertsTypesLevelAllCustomDateRange
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#             print(
#                 "\n------------------- Displaying Custom Date Range all alert types and levels ---------------------------\n")
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
#             "\n------------------- Custom Date Range -- Not displaying all alert types and levels ---------------------------\n")
#         assert False
