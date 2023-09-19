# from datetime import datetime
# import requests
# import pytest
# import globalvariables as globalvars
# import Logs as WeGuard
# import Executor as Execute
# import WeBoxpayloadinfo as payload
# import test_GETutils as utils
#
#
# def url_formatter3(policyId):
#     return "enterprise/rest/weguard-v2/webox/config/{policyId}".format(policyId=policyId)
#
#
# undosave = 'enterprise/rest/weguard-v2/fcmUpdate'
#
#
# # Get WeBox configs for iOS (Undo and Save)
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_undosave == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10184)
# def test_tc_000001_Undo_Save(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvars.BaseURL + undosave
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/undosave.txt", "r")
#         # req = json.loads(file1.read())
#         res = requests.post(url=apiUrl, headers=Headers, json=payload.undosave, timeout=globalvars.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#             print("\n\n------------------- Undo and Save is passed ---------------------------\n")
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
#     except BaseException as e:
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print("\n\n------------------- Undo and Save is failed---------------------------\n\n")
#             assert False
#
#
# # WeBox Android Policy GET
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_AndroidPolicy == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10186)
# def test_tc_000001_WeBoxAndroidPolicy(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print("\n\n------------------- Android Policy configs ---------------------------\n")
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
#     except BaseException as e:
#             print("Exception : " + str(e))
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print("\n\n------------------- No configs for Android Policy  ---------------------------\n\n")
#             assert False
#
#
# # Post method for Disabled "Allowdownload" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_AlLOWDownload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10187)
# def test_tc_000001_WeBoxAllowDownload(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledallowdownload.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledallowdownload, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Allow Download is Disabled ---------------------------\n")
#             elif res.status_code == 400:
#                     print("\n" + "400 Bad Request!" + "\n")
#                     # Add your assertions or actions for 400 Bad Request response here
#                     assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                     print("\n" + "404 Result not found!" + "\n")
#                     # Add your assertions or actions for 404 Not Found response here
#                     assert False, "Received 404 response"
#             elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!" + "\n")
#                     # Add your assertions or actions for 500 Internal Server Error response here
#                     assert False, "Received 500 response"
#             else:
#                     print("Request did not succeed! Status code:", res.status_code)
#                     assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#                 print("Exception : " + str(e))
#                 now2 = datetime.now()
#                 print("Time taken: " + str(now2 - now1))
#                 print(
#                     "\n\n------------------- Allow Download is not disabled ---------------------------\n\n")
#                 assert False
#
#
# # Post method for Disabled "AllowFileView" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_AlLOWFileView == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10188)
# def test_tc_000001_WeBox_AllowFileView(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledallowfileview.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledallowfileview, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Allow File View is disabled ---------------------------\n")
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
#     except BaseException as e:
#             print("Exception : " + str(e))
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print(
#                 "\n\n------------------- Allow File View is not disabled ---------------------------\n\n")
#             assert False
#
#
# # Post method for Disabled "Open With" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_OpenWith == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10189)
# def test_tc_000001_WeBoxOpenWith(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#           # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledopenwith.txt", "r")
#           # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledopenwith, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                print("\n" + "200 The request was a success!")
#                print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#                print("\n\n------------------- Open With is disabled---------------------------\n")
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
#     except BaseException as e:
#             print("Exception : " + str(e))
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print("\n\n------------------- OpenWith is not disabled ---------------------------\n\n")
#             assert False
#
#
# # Post method for Disabled "Show links" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_ShowLinks == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10190)
# def test_tc_000001_WeBoxconfigsShowLinks(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledshowlinks.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledshowlinks, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print("\n\n------------------- Show Links is disabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("\n\n------------------- Show Links is not disabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Disabled "Allow Download, Allow file view, open with, Show links" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_noWeBoxConfigs == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10191)
# def test_tc_000001_NoWeBoxConfigs(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/noWeBoxConfigs.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.noWeBoxConfigs, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Allow Download, Allow file view, Open with, Show links are disabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Allow Download, Allow file view, Open with, Show links are not disabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Enabled "Allow Download" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBoxEnabledAlLOWDownload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10192)
# def test_tc_000001_WeBoxEnabledAllowDownload(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledallowdownload.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledallowdownload, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Allow Download is enabled ---------------------------\n")
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
#     except BaseException as e:
#             print("Exception : " + str(e))
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print(
#                 "\n\n------------------- Allow Download is not enabled ---------------------------\n\n")
#             assert False
#
#
# # Post method for Enabled "Allow File View" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBoxEnabledAlLOWFileView == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10193)
# def test_tc_000001_WeBoxEnabledAllowFileView(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledfileview.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledfileview, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             now1 = datetime.now()
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Allow File View is enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Allow File View is not enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Enabled "OpenWith" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBoxEnabledOpenWith == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10194)
# def test_tc_000001_WeBoxEnabledOpenWith(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledopenwith.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledopenwith, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print("\n\n------------------- Open With is enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("\n\n------------------- Open With is not enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Enabled "ShowLinks" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBoxEnabledShowLinks == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10195)
# def test_tc_000001_WeBoxEnabledShowLinks(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledshowlinks.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledshowlinks, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print("\n\n------------------- Show Links is enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Show Links is not enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Disabled "ServiceTypes" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBoxDisabledServiceTypes == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10196)
# def test_tc_000001_WeBoxDisabledServiceTypes(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledservicetypes.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledservicetypes, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Service Types are disabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Service Types are not disabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Disabled "WeBox Passcode" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_EnabledServiceTypes == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10199)
# def test_tc_000001_WeBoxEnabledServiceTypes(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledservicetypes.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledservicetypes, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Service Types are enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Service Types are not enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Disabled "WeBoxPasscode" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DisabledWeBoxPasscode == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10197)
# def test_tc_000001_WeBoxDisabledWeBoxPasscode(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledweboxpasscode.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledweboxpasscode, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- WeBox Passcode is disabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- WeBox Passcode is not disabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Enabled "WeBox Passcode" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_EnabledWeBoxPasscode == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10198)
# def test_tc_000001_WeBoxEnabledWeBoxPasscode(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledweboxpasscode.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledweboxpasscode, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- WeBox Passcode is enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- WeBox Passcode is not enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Enabled "Google Drive and Dropbox" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_EnabledGoogleDriveDropbox == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10200)
# def test_tc_000001_WeBoxEnabledGoogleDriveDropbox(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enablegdrivedropbox.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledgoogledrivedropbox,
#                                 timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Google Drive and Dropbox are enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Google Drive and Dropbox are enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Enabled "SD card and Amazon S3" on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_EnabledSDcardAmazonS3 == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10201)
# def test_tc_000001_WeBoxEnabledSDcardAmazonS3(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enableds3sdcard.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledAmzazonS3SDcard,
#                                 timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Amazon S3 and SD Card are enabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Amazon S3 and SD Card are not enabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Adding a folder for SD Card on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AddingfoldersforSDcard == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10222)
# def test_tc_000001_AddingfoldersforSDcard(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingSDCardFolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingSDCardFolder, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Created SD card folder successfully ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Unable to create SD card folder ---------------------------\n\n")
#         assert False
#
#
# # Post method for Adding a folder for Google Drive on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AddingfoldersforGoogleDrive == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10223)
# def test_tc_000001_AddingfoldersforGoogleDrive(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingGoogleDrivefolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingGoogleDrivefolder,
#                                 timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Created Google Drive folder successfully ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Unable to create Google Drive folder ---------------------------\n\n")
#         assert False
#
#
# # Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AddingfoldersforAmazonS3 == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10224)
# def test_tc_000001_AddingfoldersforAmazonS3(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingAmazonS3folder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingAmazonS3folder, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Created Amazon S3 folder successfully ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Unable to create AmazonS3 folder ---------------------------\n\n")
#         assert False
#
#
# # Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AddingfoldersforDropbox == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10225)
# def test_tc_000001_AddingfoldersforDropbox(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingDropboxfolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingDropboxfolder, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Created Dropbox folder successfully ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Unable to create Dropbox folder ---------------------------\n\n")
#         assert False
#
#
# # Post method for Disabled "SD card and Amazon S3" on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DisabledSDcardAmazonS3 == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10226)
# def test_tc_000001_WeBoxDisabledSDcardAmazonS3(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DisabledSDcardAmazonS3.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.DisabledSDcardAmazonS3,
#                                 timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- SD card and Amazon S3 are disabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- SD card and Amazon S3 are not disabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Disabled "Google Drive and Dropbox" on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DisabledGoogleDriveDropbox == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10227)
# def test_tc_000001_WeBoxDisabledGoogleDriveDropbox(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DisabledGoogleDriveDropbox.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.DisabledGoogleDriveDropbox,
#                                 timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Google Drive and Dropbox are disabled ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Google Drive and Dropbox are not disabled ---------------------------\n\n")
#         assert False
#
#
# # Post method for Adding a folder for SD Card on portal for Android Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AddingfoldersforSDcard == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10228)
# def test_tc_000001_AddingfoldersforSDcard(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingSDCardFolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingSDCardFolder, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Created SD card folder successfully ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("\n\n------------------- Unable to create SD card folder ---------------------------\n\n")
#         assert False
#
#
# # Post method for Deleting a folder for Google Drive on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeletingfoldersforGoogleDrive == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10229)
# def test_tc_000001_DeletingfoldersforGoogleDrive(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DeletingGoogleDriveFolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.DeletingGoogleDriveFolder,
#                                 timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Deleted Google Drive folder successfully ---------------------------\n")
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
#     except BaseException as e:
#             print("Exception : " + str(e))
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print(
#                 "\n\n------------------- Unable to delete Google Drive folder ---------------------------\n\n")
#             assert False
#
#
# # Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeletingfoldersforSDCard == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10230)
# def test_tc_000001_DeletingfoldersforSDCard(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DeletingSDCardFolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.DeletingSDCardFolder, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Deleted SD Card folder successfully ---------------------------\n")
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
#     except BaseException as e:
#             print("Exception : " + str(e))
#             now2 = datetime.now()
#             print("Time taken: " + str(now2 - now1))
#             print(
#                 "\n\n------------------- Unable to delete SD Card folder ---------------------------\n\n")
#             assert False
#
#
# # Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeletingfoldersforDropbox == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10231)
# def test_tc_000001_DeletingfoldersforDropbox(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#             url3 = url_formatter3(policyId)
#             apiUrl = globalvars.BaseURL + url3
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DeletingDropboxFolder.txt", "r")
#             # req = json.loads(file1.read())
#             res = requests.post(url=apiUrl, headers=Headers, json=payload.DeletingDropboxFolder, timeout=globalvars.timeout)
#             curl_str1 = utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                       "\n" + "Request URL: " + apiUrl +
#                       "\n" + "Request Method: " + res.request.method +
#                       "\n" + "Status Code: " + str(res.status_code) +
#                       "\n" + "Response: " + str(res.content) + "\n")
#                 print(
#                     "\n\n------------------- Deleted Dropbox folder successfully ---------------------------\n")
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
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "\n\n------------------- Unable to delete Dropbox folder ---------------------------\n\n")
#         assert False
#
#
# # WeBox Files POST API
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_Webox_filespost == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10185)
# def test_tc_000001_WeBoxfilespost(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_Policy_IDs:
#          url3 = url_formatter3(policyId)
#         apiUrl = globalvars.BaseURL + url_formatter3
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/Weboxfiles.txt", "r")
#         # req = json.loads(file1.read())
#         res = requests.post(url=apiUrl, headers=Headers, json=payload.WeBoxFiles, timeout=globalvars.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                   "\n" + "Request URL: " + apiUrl +
#                   "\n" + "Request Method: " + res.request.method +
#                   "\n" + "Status Code: " + str(res.status_code) +
#                   "\n" + "Response: " + str(res.content) + "\n")
#             print("\n\n------------------- WeBox Files POST API ---------------------------\n")
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
#         assert res.status_code == 200
#     except BaseException as e:
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("\n\n------------------- WeBox Files POST API ---------------------------\n\n")
#         print("Exception : " + str(e))
#         assert False
