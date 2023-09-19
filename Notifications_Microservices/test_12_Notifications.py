# import datetime
# import json
#
# import pytest
# import requests
# import Executor as Execute
# import globalvariables
# import test_GETutils as Utils
# import general_payload as Generalpayload
# import WeGuardLogger as WeGuard
#
#
# # Define the GET AccountLevel Notifications
# def AccountLevelNotifications(accountId):
#     return "notification/rest/notification/all/account/{accountId}".format(accountId=accountId)
#
# POSTAccountLevelNotifications = "notification/rest/notification"
#
# def PUTAccountLevelNotifications(notificationId):
#     PUT_AccountLevelNotification = "notification/rest/notification/{notificationId}".format(notificationId=notificationId)
#     return PUT_AccountLevelNotification
#
# def GETNotificationsByPolicyLevel(policyId):
#     return "notification/rest/notification/all/policy/{policyId}".format(policyId=policyId)
#
# POSTPolicyLevelNotifications = "notification/rest/notification"
#
# def PUTNotifications_PolicyLevel(notificationId):
#     PUT_PolicyLevelNotification = "notification/rest/notification/{notificationId}".format(notificationId=notificationId)
#     return PUT_PolicyLevelNotification
#
# # GET Policy Level Geofence
# def GETPolicyLevelGeofence(policyId):
#     return "notification/rest/notification/geofence/{policyId}".format(policyId=policyId)
#
# POSTGeofence= "notification/rest/notification/geofence"
#
# # Define PUTGeofence as a function that generates the API endpoint URL
# def PUTGeofences(mongoDBId):
#     return f"notification/rest/notification/geofence/{mongoDBId}".format(mongoDBId=mongoDBId)
#
# # Delete Policy Level Geofence
# def DeleteGeofence(policyId):
#     return "notification/rest/notification/geofence/{policyId}".format(policyId=policyId)
#
# def TimespentGeofence(accountId, page, size, start, end):
#    GeofenceTimespent = "notification/rest/timespent/account/{accountId}?page={page}&size={size}&start={start}&end={end}".format(accountId=accountId, page=page, size=size, start=start, end=end)
#    return GeofenceTimespent
#
# # GET method to get all the Account Level Notifications
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1101_Notifications_AccountLevel_GET == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11001)
# def test_tc_1101_GET_AccountLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         GetAccountLevelNotifications = AccountLevelNotifications(globalvariables.accountId)
#         apiUrl = globalvariables.BaseURL + GetAccountLevelNotifications
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!" + "\n")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#             response_data = json.loads(res.content)
#             entities = response_data.get('entities', [])  # Check if 'entities' is present, use an empty list if not
#             if entities:
#                 Generalpayload.AccountID = entities[0].get('accountId', '')  # Check if 'accountId' is present, use an empty string if not
#                 print("Account ID:", Generalpayload.AccountID)
#                 # Initialize a list to store all 'id' values
#                 id_list = []
#                 # Loop through the entities and extract 'id' for each entity
#                 for entity in entities:
#                     entity_id = entity.get('id', '')  # Check if 'id' is present, use an empty string if not
#                     id_list.append(entity_id)
#                 # Now id_list contains all the 'id' values
#                 Generalpayload.getAccountLevelNotificationId = id_list
#                 print("Notification IDs:", id_list)
#             else:
#                 print("No entities found in the response.")
#             print(
#                 "\n------------------- GET method to get all the Account Level Notifications ---------------------------\n")
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
#     except Exception as e:
#         print("Exception : " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to GET method to get all the Account Level Notifications ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # POST method to get all the Account Level Notifications with Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1102_Notifications_AccountLevel_POST == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11002)
# def test_tc_1102_POST_AccountLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#             apiUrl = globalvariables.BaseURL + POSTAccountLevelNotifications
#             Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#             Generalpayload.PostAccountLevelAlertConfig["accountId"] = globalvariables.accountId
#             Info = Generalpayload.PostAccountLevelAlertConfig
#             res = requests.post(url=apiUrl, headers=Headers, json=Info,
#                                 timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 globalvariables.Account_notification_ids = json.loads(res.content)['entity']['id']
#                 print("\nAccount Level Notification IDs:", Generalpayload.getAccountLevelNotificationId)
#                 print(
#                     "\n------------------- POST method to get all the Account Level Notifications with Email Address ---------------------------\n")
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
#                 assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception : " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to POST method to get all the Account Level Notifications with Email Address ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # PUT method to update Account Level Notifications with Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1103_Notifications_AccountLevel_PUT == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11003)
# def test_tc_1103_PUT_AccountLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for notification_id in Generalpayload.getAccountLevelNotificationId:
#             apiUrl = globalvariables.BaseURL + PUTAccountLevelNotifications(notification_id)
#             headers = {'Authorization': f'Bearer {globalvariables.bearerToken}'}
#             Generalpayload.PutAccountLevelNotifications["accountId"] = globalvariables.accountId
#             res = requests.put(url=apiUrl, headers=headers, json=Generalpayload.PutAccountLevelNotifications,
#                                timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print("\n------------------- PUT method to update Account Level Notifications with Email Address ---------------------------\n")
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
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to PUT method to update Account Level Notifications with Email Address ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # GET method to get policy level Notifications
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1104_Notification_PolicyLevel_GET == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11006)
# def test_tc_1104_GET_PolicyLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for policyId in globalvariables.Android_Policy_IDs:
#             apiUrl = globalvariables.BaseURL + GETNotificationsByPolicyLevel(policyId)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n------------------- GET method to get policy level Notifications ---------------------------\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to GET method to get policy level Notifications ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # POST method to get all the Policy Level Notifications with Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1106_Notifications_PolicyLevel_POST == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11004)
# def test_tc_1106_POST_PolicyLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         apiUrl = globalvariables.BaseURL + POSTPolicyLevelNotifications
#         Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#         # Loop through policy IDs and send POST requests
#         for policy_id in globalvariables.Android_Policy_IDs:
#             # Update the payload with the current policy ID
#             Generalpayload.PostPolicyLevelAlertConfig["accountId"] = Generalpayload.AccountID
#             Generalpayload.PostPolicyLevelAlertConfig["policyId"] = policy_id
#             Info = Generalpayload.PostPolicyLevelAlertConfig
#             res = requests.post(url=apiUrl, headers=Headers, json=Info,
#                                 timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 # Extract the notification ID from the response
#                 notification_id = json.loads(res.content)['entity']['id']
#                 # Append the notification ID to the list
#                 Generalpayload.getPolicyLevelNotificationId.append(notification_id)
#                 print("\nPolicy Level Notification IDs:", Generalpayload.getPolicyLevelNotificationId)
#                 print(
#                     "\n------------------- POST method to get all the Policy Level Notifications with Email Address ---------------------------\n")
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
#                 assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception : " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to POST method to get all the Policy Level Notifications with Email Address ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # PUT method to update Policy Level Notifications with Email Address
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1107_Notifications_PolicyLevel_PUT == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11007)
# def test_tc_1107_PUT_PolicyLevel_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for notification_ids in Generalpayload.getPolicyLevelNotificationId:
#             for policy_ids in globalvariables.Android_Policy_IDs:
#                 apiUrl = globalvariables.BaseURL + PUTNotifications_PolicyLevel(notification_ids)
#                 headers = {'Authorization': f'Bearer {globalvariables.bearerToken}'}
#                 Generalpayload.PutPolicyLevelNotifications["accountId"] = globalvariables.accountId
#                 Generalpayload.PutPolicyLevelNotifications["policyId"] = policy_ids
#                 res = requests.put(url=apiUrl, headers=headers, json=Generalpayload.PutAccountLevelNotifications,
#                                    timeout=globalvariables.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print("\n" + "Header: " + str(res.headers) +
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Response: " + str(res.content) + "\n")
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print("\n" + "Header: " + str(res.headers) +
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Response: " + str(res.content) + "\n")
#                     print(
#                         "------------------- PUT method to update Policy Level Notifications with Email Address ---------------------------\n")
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
#                     assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to PUT method to update Policy Level Notifications with Email Address ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # Geofences
# # POST method to create/add the Geofence at the policy level
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1108_Notification_PolicyLevel_Geofence_POST == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11008)
# def test_tc_1108_POST_PolicyLevel_Notifications_Geofence(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for policyId in globalvariables.Android_Policy_IDs:
#             for geofenceId in Generalpayload.GeofenceIds:
#                 POSTGeofencePayload = {
#                     "geofenceIdList": [geofenceId],
#                     "policyId": policyId
#                 }
#                 apiUrl = globalvariables.BaseURL + POSTGeofence
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#                 res = requests.post(url=apiUrl, headers=Headers, json=POSTGeofencePayload, timeout=globalvariables.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 if res.status_code == 200:
#                     print(curl_str1)
#                     print("\n" + "200 The request was a success!")
#                     print("\n" + "Header: " + str(res.headers) +
#                           "\n" + "Request URL: " + apiUrl +
#                           "\n" + "Request Method: " + res.request.method +
#                           "\n" + "Status Code: " + str(res.status_code) +
#                           "\n" + "Response: " + str(res.content) + "\n")
#                     print(
#                         "\n------------------- POST method to get policy level Geofence based on geofence list ---------------------------\n")
#                 else:
#                     if res.status_code == 400:
#                         print("\n" + "400 Bad Request!" + "\n")
#                     elif res.status_code == 404:
#                         print("\n" + "404 Result not found!" + "\n")
#                     elif res.status_code == 500:
#                         print("\n" + "500 Internal Server Error!" + "\n")
#                     else:
#                         print("Request did not succeed! Status code:", res.status_code)
#                     assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to POST method to get policy level Geofence based on geofence list ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
# # GET method to get policy level Geofence
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1109_Notification_PolicyLevel_Geofence_GET == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11009)
# def test_tc_1109_GET_PolicyLevel_Notifications_Geofence(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for policyId in globalvariables.Android_Policy_IDs:
#             apiUrl = globalvariables.BaseURL + GETPolicyLevelGeofence(policyId)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 # Parse the JSON response
#                 response_data = json.loads(res.content)
#                 # Extract 'geofenceId', 'geofenceTypes' and 'id' from the 'entities' list
#                 for entity in response_data.get("entities", []):
#                     geofence_id = entity.get("geofenceId")
#                     geofence_mongodb_id = entity.get("id")
#                     geofence_type = entity.get("geofenceType")
#
#                     #                if geofence_id and geofence_mongodb_id and geofence_type:
#                     #                        print(f"\nGeofence ID: {geofence_id}")
#                     #                        print(f" MongoDB ID : {geofence_mongodb_id}")
#                     #                        print(f"Geofence Type : {geofence_type}\n")
#
#                     # Append the data to respective lists
#                     Generalpayload.GeofenceIDS.append(geofence_id)
#                     Generalpayload.Geofence_MongoDB_IDs.append(geofence_mongodb_id)
#                     Generalpayload.GeofenceTypes.append(geofence_type)
#
#                 # Now you have all the geofence IDs, MongoDB IDs, and geofence types in separate arrays
#                 print("All Geofence IDs:", ", ".join(map(str, Generalpayload.GeofenceIDS)) + "\n")
#                 print("All MongoDB IDs:", ", ".join(map(str, Generalpayload.Geofence_MongoDB_IDs)) + "\n")
#                 print("All Geofence Types:", ", ".join(map(str, Generalpayload.GeofenceTypes)) + "\n")
#                 print(
#                     "\n------------------- GET method to get policy level Notifications ---------------------------\n")
#             elif res.status_code == 400:
#                print("\n" + "400 Bad Request!" + "\n")
#             elif res.status_code == 404:
#                print("\n" + "404 Result not found!" + "\n")
#             elif res.status_code == 500:
#                print("\n" + "500 Internal Server Error!" + "\n")
#             else:
#                print("Request did not succeed! Status code:", res.status_code)
#                assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to GET method to get policy level Notifications ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
#
# # PUT method to update the policy level Geofence
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1110_Notification_PolicyLevel_Geofence_PUT == 0, reason="Skip test")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11010)
# def test_tc_1110_PUT_PolicyLevel_Notifications_Geofence(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for mongodbId in Generalpayload.Geofence_MongoDB_IDs:
#             apiUrl = globalvariables.BaseURL + PUTGeofences(mongodbId)
#             Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#             PUTGeofence = {
#                 "emailList": [Generalpayload.random_gmail_address],
#                 "enabled": Generalpayload.enabled_values
#             }
#             res = requests.put(url=apiUrl, headers=Headers, json=PUTGeofence, timeout=globalvariables.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             # Convert the dictionary to a string
#             PUTGeofence_str = str(PUTGeofence)
#             if res.status_code == 200:
#                 print(curl_str1)
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Request Payload: " + PUTGeofence_str +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n------------------- PUT method to update policy level Geofence ---------------------------\n")
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
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to update policy level Geofence with PUT method  ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
# # DELETE method to delete the Geofence based on Geofence ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1111_Notification_PolicyLevel_Geofence_DELETE == 0, reason="Delete the geofence")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11011)
# def test_tc_1111_DELETE_PolicyLevel_Notifications_Geofence(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for policyId in globalvariables.Android_Policy_IDs:
#             for geofenceIdList in Generalpayload.GeofenceIds:
#              apiUrl = globalvariables.BaseURL + DeleteGeofence(policyId)
#              Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#              DeleteGeofencePayload = [geofenceIdList]
#              res = requests.delete(url=apiUrl, headers=Headers, json=DeleteGeofencePayload, timeout=globalvariables.timeout)
#              curl_str1 = Utils.getCurlEquivalent(res)
#              print(curl_str1)
#              if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n------------------- DELETE method to get policy level geofence ---------------------------\n")
#              elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#              elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#              elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#              else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to delete the policy level geofence with DELETE method ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
# # Skipping this testcases, reason: It will delete the Geofence Notifications
# # DELETE method to delete the Geofence Notifications
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1112_Notification_PolicyLevel_Geofence_Notifications_DELETE == 0, reason="Delete the Geofence Notifications")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11012)
# def test_tc_1112_DELETE_PolicyLevel_Geofence_Notifications(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for policyId in globalvariables.Android_Policy_IDs:
#             for geofenceType_value in Generalpayload.geofenceType_values:
#                 for enabled_value in Generalpayload.enabled_values:
#                     # Update the payload with the current values
#                     Generalpayload.DeleteGeofenceNotificationsPayload["geofenceType"] = geofenceType_value
#                     Generalpayload.DeleteGeofenceNotificationsPayload["enabled"] = enabled_value
#                     apiUrl = globalvariables.BaseURL + DeleteGeofence(policyId)
#                     Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#                     Json = Generalpayload.DeleteGeofenceNotificationsPayload
#                     res = requests.delete(url=apiUrl, headers=Headers, json=Json, timeout=globalvariables.timeout)
#                     curl_str1 = Utils.getCurlEquivalent(res)
#                     print(curl_str1)
#                     if res.status_code == 200:
#                         print("\n" + "200 The request was a success!")
#                         print("\n" + "Header: " + str(res.headers) +
#                               "\n" + "Request URL: " + apiUrl +
#                               "\n" + "Request Method: " + res.request.method +
#                               "\n" + "Status Code: " + str(res.status_code) +
#                               "\n" + "Response: " + str(res.content) + "\n")
#                         print(
#                             "\n------------------- DELETE method to delete policy level geofence notifications ---------------------------\n")
#                     elif res.status_code == 400:
#                         print("\n" + "400 Bad Request!" + "\n")
#                     elif res.status_code == 404:
#                         print("\n" + "404 Result not found!" + "\n")
#                     elif res.status_code == 500:
#                         print("\n" + "500 Internal Server Error!" + "\n")
#                     else:
#                         print("Request did not succeed! Status code:", res.status_code)
#                         assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to delete the policy level geofence notifications with DELETE method ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
#
# # POST method to get the time spent details in the Geofence for all policies, devices and Geofences
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_1113_Notification_Timespent_Geofence_ALL_Policies_Device_Geofences_POST == 0, reason="Takes ~30 minutes time to execute for all policies, devices and Geofences")
# @pytest.mark.positivetest
# @pytest.mark.notifications
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=11013)
# def test_tc_1113_POST_Timespent_Geofence(url):
#     now1 = datetime.datetime.now()
#     if globalvariables.bearerToken == '':
#         pytest.skip("Empty Bearer token, Skipping test")
#     try:
#         for policyId in globalvariables.Android_Policy_IDs:
#             for android_device_id in globalvariables.Android_DeviceIDs:
#                  for geofenceId in Generalpayload.GeofenceIDS:
#                     apiUrl = globalvariables.BaseURL + TimespentGeofence(globalvariables.accountId,
#                                                                          globalvariables.page_1,
#                                                                          globalvariables.page_1000,
#                                                                          globalvariables.isostart,
#                                                                          globalvariables.isoend)
#                     Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
#                     # Time spent in geofence
#                     TimespentGeofencePayload = {
#                         "policyId": policyId,
#                         "deviceIdList": [android_device_id],
#                         "geofenceId": geofenceId
#                     }
#                     res = requests.post(url=apiUrl, headers=Headers, json=TimespentGeofencePayload,
#                                         timeout=globalvariables.timeout)
#                     curl_str1 = Utils.getCurlEquivalent(res)
#                     print(curl_str1)
#                     Timespent = res.json()  # Parse JSON response
#                     if res.status_code == 200:
#                         print("\n" + "200 The request was a success!")
#                         print("\n" + "Header: " + str(res.headers) +
#                               "\n" + "Request URL: " + apiUrl +
#                               "\n" + "Request Method: " + res.request.method +
#                               "\n" + "Status Code: " + str(res.status_code) +
#                               "\n" + "Request Payload: " + json.dumps(Timespent) +  # Convert to JSON string
#                               "\n" + "Response: " + str(res.content) + "\n")
#                         print(
#                             "\n------------------- POST method to get geofence time spent ---------------------------\n")
#                     elif res.status_code == 400:
#                         print("\n" + "400 Bad Request!" + "\n")
#                     elif res.status_code == 404:
#                         print("\n" + "404 Result not found!" + "\n")
#                     elif res.status_code == 500:
#                         print("\n" + "500 Internal Server Error!" + "\n")
#                     else:
#                         print("Request did not succeed! Status code:", res.status_code)
#                         assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.datetime.now()
#         print(
#             "\n------------------- Unable to get geofence time spent with POST method ---------------------------\n")
#         print("Time taken: " + str(now2 - now1))
#         assert False, f"An exception occurred: {e}"
