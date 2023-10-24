# import json
# from datetime import datetime
# import pytest
# import requests
# import Executor as Execute
# import globalvariables as Globalinfo
# import test_GETutils as Utils
# import general_payload as requestinfo
#
#
# def AndroidPolicy(policyId):
#     GETAndroidPolicy = "enterprise/rest/weguard-v2/policy/{policyId}".format(policyId=policyId)
#     return GETAndroidPolicy
#
#
# def AndroidAppsData(activationCode, productActivationCode):
#     GETAndroidAppsData = "enterprise/rest/weguard-v2/appdata/getApp/actCode/{activationCode}/pactCode/{productActivationCode}".format(
#         activationCode=activationCode, productActivationCode=productActivationCode)
#     return GETAndroidAppsData
#
#
# PlayStoreAppList = "enterprise/rest/weemm/product/list"
#
#
# def GETAndroidLocationTrackConfig(policyId):
#     LocationTrackConfig = "enterprise/rest/locationtrackconfig/{policyId}".format(policyId=policyId)
#     return LocationTrackConfig
#
#
# def GETAndroidDataUsage(policyId):
#     AndroidDataUsage = "enterprise/rest/config/datausage/{policyId}".format(policyId=policyId)
#     return AndroidDataUsage
#
#
# def GETAndroidAPNSettingID(apnSettingId):
#     APNSettingID = "enterprise/rest/apn-setting/{apnSettingId}".format(apnSettingId=apnSettingId)
#     return APNSettingID
#
#
# def GETAndroidKioskPersonaImage(policyId):
#     KioskPersonaImage = "enterprise/rest/kiosk-persona-image?policyId={policyId}".format(policyId=policyId)
#     return KioskPersonaImage
#
#
# def GETAndroidGenericQRGeneration(policyId):
#     AndroidQR = "enterprise/rest/weguard-v2/qr/generic/generation/{policyId}".format(policyId=policyId)
#     return AndroidQR
#
#
# def GETAndroidDisabledApps(policyId):
#     AndroidDisabledApps = "enterprise/rest/disabledapps/{policyId}".format(policyId=policyId)
#     return AndroidDisabledApps
#
#
# def GETAndroidTimeFence(timeFenceConfigId):
#     AndroidTimeFence = "enterprise/rest/timefence/{timeFenceConfigId}".format(timeFenceConfigId=timeFenceConfigId)
#     return AndroidTimeFence
#
#
# # GET -- Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4001_GET_Android_Policy_By_ID == 0, reason="GET - Android Policy")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400001)
# def test_tc_4001_Android_Policy_By_ID_GET(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in Globalinfo.Android_Policy_IDs:
#             apiUrl = Globalinfo.BaseURL + AndroidPolicy(policyId)
#             Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#             res = requests.get(url=apiUrl, headers=Headers)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n\n")
#
#                 # Decode the JSON response
#                 response = res.content.decode('utf-8')
#                 parsed_response = json.loads(response)
#
#                 # Extract Android policy name
#                 android_policy_name = parsed_response['entity']['name']
#                 if android_policy_name:
#                     Globalinfo.Android_Policy_Name.append(android_policy_name)
#                     print("Policy Name:", android_policy_name, "\n")
#                 else:
#                     print("Policy Name not found in the response.")
#
#                 # Extract APN setting ID
#                 apn_setting_id = parsed_response['entity']['apnSettingId']
#                 if apn_setting_id:
#                     Globalinfo.APNSettingID.append(apn_setting_id)
#                     print("APN Setting ID:", apn_setting_id, "\n")
#                 else:
#                     print("APN Setting ID not found in the response." + "\n")
#
#                 # Extract geofences if they exist
#                 geofences = parsed_response.get('entity', {}).get('geofences', [])
#                 geofence_policy_ids = []
#
#                 if geofences:
#                     for geofence in geofences:
#                         geofence_policy_id = geofence.get('geofencePolicyId')
#                         if geofence_policy_id is not None:
#                             geofence_policy_ids.append(geofence_policy_id)
#
#                 if geofence_policy_ids:
#                     requestinfo.geofencePolicyConfigId.extend(geofence_policy_ids)
#                     print("Geofence Policy Config IDs: ", geofence_policy_ids, "\n")
#                 else:
#                     print("No geofences with 'geofencePolicyId' found in the response." + "\n")
#                     print("Geofence Policy IDs of all Android Policies: ", requestinfo.geofencePolicyConfigId, "\n")
#
#                 # Extract and handle timeFencePolicyConfigs if they exist
#                 time_fence_config = parsed_response.get('entity', {}).get('timeFencePolicyConfigs')
#                 if time_fence_config is not None:
#                     time_fence_config_id = time_fence_config.get('id')
#                     if time_fence_config_id:
#                         Globalinfo.timefenceId.append(time_fence_config_id)
#                         print("Time Fence Config ID:", time_fence_config_id, "\n")
#                     else:
#                         print("No Time Fence Config ID found in timeFencePolicyConfigs." + "\n")
#                 else:
#                     print("No Time Fence Configs available in the response." + "\n")
#                     print("Time Fence Config IDs of all Android Policies: ", Globalinfo.timefenceId, "\n")
#
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android Policy Failed ---------------------------\n\n")
#         assert False
#
# # GET -- Android Apps Data by Activation and Product Activation Code
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4002_GET_Android_AppsData == 0, reason="GET - Android Apps Data")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400002)
# def test_tc_4002_Android_AppsData(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = Globalinfo.BaseURL + AndroidAppsData(Globalinfo.activationCode, Globalinfo.productActivationCode)
#         Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#         res = requests.get(url=apiUrl, headers=Headers)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!" + "\n")
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                 "\n" + "Request URL: " + apiUrl +
#                 "\n" + "Request Method: " + res.request.method +
#                 "\n" + "Status Code: " + str(res.status_code) +
#                 "\n" + "Response: " + str(res.content) + "\n\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android Apps Data Failed ---------------------------\n\n")
#         assert False
#
#
# # GET -- Play Store Apps/WEEMM Apps List
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4003_GET_Android_Play_Store_AppsList == 0, reason="GET - Android Play Store Apps")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400003)
# def test_tc_4003_Android_Playstore_AppsList(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = Globalinfo.BaseURL + PlayStoreAppList
#         Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#         res = requests.get(url=apiUrl, headers=Headers)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!" + "\n")
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                 "\n" + "Request URL: " + apiUrl +
#                 "\n" + "Request Method: " + res.request.method +
#                 "\n" + "Status Code: " + str(res.status_code) +
#                 "\n" + "Response: " + str(res.content) + "\n\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android Play Store Apps List Failed ---------------------------\n\n")
#         assert False
#
#
# # GET -- Location Track Config by Policy ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4004_GET_Android_Location_Track_Config == 0,
#                     reason="GET - Android Location Track Config")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400004)
# def test_tc_4004_Android_Location_Track_Config(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in Globalinfo.Android_Policy_IDs:
#             apiUrl = Globalinfo.BaseURL + GETAndroidLocationTrackConfig(policyId)
#             Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#             res = requests.get(url=apiUrl, headers=Headers)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android Location Track Config Failed ---------------------------\n\n")
#         assert False
#
#
# # GET -- Location Track Config by Policy ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4005_GET_Android_DataUsage == 0,
#                     reason="GET - Android Data Usage")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400005)
# def test_tc_4005_Android_DataUsage(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in Globalinfo.Android_Policy_IDs:
#             apiUrl = Globalinfo.BaseURL + GETAndroidDataUsage(policyId)
#             Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#             res = requests.get(url=apiUrl, headers=Headers)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android Data Usage Failed ---------------------------\n\n")
#         assert False
#
#
# # GET -- APN Setting by ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4006_GET_Android_APN_Setting_ID == 0,
#                     reason="GET - Android APN Setting")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400006)
# def test_tc_4006_Android_APNSettingID(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for apnSettingId in Globalinfo.APNSettingID:
#             apiUrl = Globalinfo.BaseURL + GETAndroidAPNSettingID(apnSettingId)
#             Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#             res = requests.get(url=apiUrl, headers=Headers)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android APN Setting Failed ---------------------------\n\n")
#         assert False
#
#
# # GET -- Kiosk Persona Image by Policy ID
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4007_GET_Android_Kiosk_Persona_Image == 0,
#                     reason="GET - Android Kiosk Persona Image")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=400007)
# def test_tc_4007_Android_Kiosk_Persona_Image(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for kioskpolicyId in Globalinfo.Android_Kiosk_Policy_IDs:
#             apiUrl = Globalinfo.BaseURL + GETAndroidKioskPersonaImage(kioskpolicyId)
#             Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#             res = requests.get(url=apiUrl, headers=Headers)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!" + "\n")
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- GET Android Kiosk Persona Image Failed ---------------------------\n\n")
#         assert False
#
#
# # GET method to get the Generic QR Generation
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4008_GET_Android_GenericQRGeneration == 0,
#                     reason="Android Generic QR Generation is skipped")
# @pytest.mark.poitivetest
# @pytest.mark.contacts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=400008)
# def test_tc_4008_GET_Android_Generic_QR_Generation(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in Globalinfo.Android_Policy_IDs:
#             apiUrl = Globalinfo.BaseURL + GETAndroidGenericQRGeneration(policyId)
#             Headers = {'Authorization': 'Bearer {}'.format(Globalinfo.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=Globalinfo.timeout)
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
#             "------------- Failed to display the Generic QR Generation information when the policy is launched ---------------------------\n\n")
#         assert False
#
#
# # GET method to get the Generic QR Generation
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4009_GET_Android_Disabled_Apps == 0, reason="Android Disabled Apps is skipped")
# @pytest.mark.poitivetest
# @pytest.mark.contacts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=400009)
# def test_tc_4009_GET_Android_Generic_QR_Generation(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in Globalinfo.Android_Policy_IDs:
#             apiUrl = Globalinfo.BaseURL + GETAndroidDisabledApps(policyId)
#             Headers = {'Authorization': 'Bearer {}'.format(Globalinfo.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=Globalinfo.timeout)
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
#             "------------- Failed to display the Android Disabled Apps information when the policy is launched ---------------------------\n\n")
#         assert False
#
#
# # GET method to get the Generic QR Generation
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_4010_GET_Android_Time_Fence == 0, reason="Android Time Fence is skipped")
# @pytest.mark.poitivetest
# @pytest.mark.contacts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=400010)
# def test_tc_4010_GET_Android_Time_Fence(url):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for timefenceConfigID in Globalinfo.timefenceId:
#             apiUrl = Globalinfo.BaseURL + GETAndroidTimeFence(timefenceConfigID)
#             Headers = {'Authorization': 'Bearer {}'.format(Globalinfo.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=Globalinfo.timeout)
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
#             "------------- Failed to display the time fence information when the policy is launched ---------------------------\n\n")
#         assert False
