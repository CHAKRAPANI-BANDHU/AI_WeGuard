# from datetime import datetime
# import requests
# import pytest
# import globalvariables as globalvars
# import Logs as WeGuard
# import Executor as Execute
# import test_GETutils as Utils
# import json
# import WeBoxpayloadinfo as WeBox
#
# events = 'enterprise/rest/weguard/logs/events'
#
# def url_formatter5(actcode, page, limit):
#     url5 = "enterprise/rest/weguard-v2/webox/upload/folder/{actcode}/shared?page={page}&limit={limit}".format(actcode=actcode, page=page, limit=limit)
#     return url5
#
# def url_formatter6(actcode, page, limit):
#     url6 = "enterprise/rest/weguard-v2/webox/upload/folder/{actcode}/group?page={page}&limit={limit}".format(actcode=actcode, page=page, limit=limit)
#     return url6
#
# createglobalsharedpolicygroupsfolders='enterprise/rest/weguard-v2/webox/upload/folder/create'
#
# config='enterprise/rest/weguard-v2/webox/upload/config'
#
# def url_formatter7(policyId):
#     url7 = 'enterprise/rest/weguard-v2/webox/upload/config/{policyId}/Policy'.format(policyId=policyId)
#     return url7
#
# def url_formatter8(foldername, page, limit, start, end):
#     url8 = 'enterprise/rest/weguard-v2/webox/upload/files/shared/{foldername}?page={page}&limit={limit}&from={start}&to={end}'.format(foldername=foldername, page=page, limit=limit, start=start, end=end)
#     return url8
#
# def url_formatter9(policyId, foldername, page, limit, start, end):
#     url9 = 'enterprise/rest/weguard-v2/webox/upload/files/policy/{policyId}/{foldername}?page={page}&limit={limit}&from={start}&to={end}'.format(policyId=policyId, foldername=foldername, page=page, limit=limit, start=start, end=end)
#     return url9
#
# def url_formatter10(foldername, page, limit):
#     url10 = "enterprise/rest/weguard-v2/webox/upload/files/shared/{foldername}?page={page}&limit={limit}".format(foldername=foldername, page=page, limit=limit)
#     return url10
#
# def url_formatter11(policyId, foldername, page, limit):
#     url11 = "enterprise/rest/weguard-v2/webox/upload/files/policy/{policyId}/{foldername}?page={page}&limit={limit}".format(policyId=policyId, foldername=foldername, page=page, limit=limit)
#     return url11
#
# def url_formatter12(actcode, pactcode):
#     url12 = "enterprise/rest/weguard-v2/webox/upload/config/{actcode}/{pactcode}/Shared".format(actcode=actcode, pactcode=pactcode)
#     return url12
#
#
# # Post method for Shared FoldersWeBox upload config without sign
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithoutsign == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10181)
# def test_tc_000001_SharedFoldersWeBoxuploadconfigwithoutsign(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvars.BaseURL + config
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.SharedFolderconfigwithoutSign,
#                             timeout=globalvars.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content))
#             WeGuard.logger.debug(
#                 "\n\n--------------------------- Shared Folders WeBox upload config without sign passed  ---------------------------\n")
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
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Shared Folders WeBox upload config without sign failed ---------------------------\n\n")
#         assert False
#
#
# # Post method for Shared Folders WeBox upload config with sign
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithsign == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10185)
# def test_tc_000001_SharedFoldersWeBoxuploadconfigwithsign(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvars.BaseURL + config
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         WeBox.SharedFolderconfigwithSign["activationCode"] = globalvars.activationCode
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.SharedFolderconfigwithSign,
#                             timeout=globalvars.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content))
#             WeGuard.logger.debug(
#                 "\n\n--------------------------- Shared Folders WeBox upload config with sign passed ---------------------------\n")
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
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Shared Folders WeBox upload config with sign failed ---------------------------\n\n")
#         assert False
#
#
# # GET method to view WeBox upload files in policy for global shared folders
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_GlobalSharedFolders_viewfilesinsharedfolder == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10239)
# def test_tc_000001_ViewFilesinSharedFolderafterclickingeyeicon(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for name in WeBox.sharedfolderslist:
#             viewfoldersinsharedfolder = url_formatter8(name, globalvars.page_1, globalvars.page_100, WeBox.isostart,
#                                                        WeBox.isoend)
#             apiUrl = globalvars.BaseURL + viewfoldersinsharedfolder
#             Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalvars.timeout)
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print("\n" + "Header: " + str(res.headers) +
#                                      "\n" + "Request URL: " + apiUrl +
#                                      "\n" + "Request Method: " + res.request.method +
#                                      "\n" + "Status Code: " + str(res.status_code) +
#                                      "\n" + "Response: " + str(res.content))
#                 WeGuard.logger.debug(
#                     "\n\n--------------------------- Files are available in globals shared folder ---------------------------\n")
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
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Files are not available in globals shared folder ---------------------------\n\n")
#         assert False
#
#
# # GET method to view WeBox upload files in policy for policy group folders
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGroupsFolders_viewfilesinpolicyfolder == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10240)
# def test_tc_000001_ViewFilesinPolicyFoldersafterclickingoneyeicon(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_profile_ids:
#             for name in WeBox.policyfolderslist:
#                 viewfilesinpolicyfolders = url_formatter9(policyId, name, globalvars.page_1, globalvars.page_100,
#                                                           WeBox.isostart, WeBox.isoend)
#                 # viewfilesinpolicyfolders = url_formatter9(globalvars.Android_profile_ids, 'AI Documents', globalvars.page_1, globalvars.page_100, WeBox.isostart, WeBox.isoend)
#                 apiUrl = globalvars.BaseURL + viewfilesinpolicyfolders
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#                 res = requests.get(url=apiUrl, headers=Headers, timeout=globalvars.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print("\n" + "Header: " + str(res.headers) +
#                                          "\n" + "Request URL: " + apiUrl +
#                                          "\n" + "Request Method: " + res.request.method +
#                                          "\n" + "Status Code: " + str(res.status_code) +
#                                          "\n" + "Response: " + str(res.content))
#                     WeGuard.logger.debug(
#                         "\n\n--------------------------- Files are available in policy groups folder ---------------------------\n")
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
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Files are not available in policy groups folder ---------------------------\n\n")
#         assert False
#
#
# # GET method to view files in policy for global shared folders upon clicking on clear
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_GlobalSharedFolders_filesbyclickingonclearinsharedfolders == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10241)
# def test_tc_000001_FolderNamesinGlobalSharedFolders(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         sharedgroupfiles = url_formatter10(globalvars.activationCode, globalvars.page_1, globalvars.page_100)
#         apiUrl = globalvars.BaseURL + sharedgroupfiles
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvars.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             WeBox.sharedfolderslist = json.loads(res.content)['entities']
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content))
#             WeGuard.logger.debug(
#                 "\n\n--------------------------- Folder names are available upon clicking on clear in shared folders ---------------------------\n")
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
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Folder names are not available upon clicking on clear in shared folders ---------------------------\n\n")
#         assert False
#
#
# # GET method to view files in policy for policy group folders upon clicking on clear
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGroupsFolders_filesbyclickingonclearinpolicyfolders == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10242)
# def test_tc_000001_FilesinPolicyGroupFolders(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalvars.Android_profile_ids:
#             for name in WeBox.policyfolderslist:
#                 policygroupfiles = url_formatter11(policyId, name, globalvars.page_1, globalvars.page_100)
#                 # policygroupfiles = url_formatter11(globalvars.Android_profile_ids, 'AI Documents', globalvars.page_1, globalvars.page_100)
#                 apiUrl = globalvars.BaseURL + policygroupfiles
#                 Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#                 res = requests.get(url=apiUrl, headers=Headers, timeout=globalvars.timeout)
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print("\n" + "Header: " + str(res.headers) +
#                                          "\n" + "Request URL: " + apiUrl +
#                                          "\n" + "Request Method: " + res.request.method +
#                                          "\n" + "Status Code: " + str(res.status_code) +
#                                          "\n" + "Response: " + str(res.content))
#                     WeGuard.logger.debug(
#                         "\n\n--------------------------- Files are available upon clicking on clear in policy group folders ---------------------------\n")
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
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Files are not available upon clicking on clear in policy group folders ---------------------------\n\n")
#         assert False
#
#
# # GET method to configs of shared folders upon clicking on setting icon(view config)
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_SharedFolders_config == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10244)
# def test_tc_000001_SharedFoldersConfig(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         sharedgroupconfig = url_formatter12(globalvars.activationCode, globalvars.productActivationCode)
#         apiUrl = globalvars.BaseURL + sharedgroupconfig
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvars.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content))
#             WeGuard.logger.debug(
#                 "\n\n--------------------------- Get the configs of Shared Folders Pass ---------------------------\n")
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
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- Get the configs of Shared Folders Pass Fail ---------------------------\n\n")
#         WeGuard.logger.error("Exception : " + str(e))
#         assert False
#
#
# # POST method to download pdf
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_DeviceUploads_pdf == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10243)
# def test_tc_000001_DownloadPDF(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         pdf = 'uploader/download/pdf'
#         apiUrl = globalvars.BaseURL + pdf
#         # compact_obj = json.dumps(WeBox.pdf)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.pdf, timeout=globalvars.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content))
#             WeGuard.logger.debug(
#                 "\n\n--------------------------- PDF file is downloaded successfully ---------------------------\n")
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
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- PDF file is not downloaded successfully ---------------------------\n\n")
#         WeGuard.logger.error("Exception : " + str(e))
#         assert False
#
#
# # POST method to download zip
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_DeviceUploads_zip == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10447)
# def test_tc_000001_DownloadZIP(url):
#     now1 = datetime.now()
#     if globalvars.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         zip = 'uploader/download/zip'
#         apiUrl = globalvars.BaseURL + zip
#         # testing = jsonpickle.encode(WeBox.zip)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvars.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.Zip, timeout=globalvars.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content))
#             WeGuard.logger.debug(
#                 "\n\n--------------------------- ZIP file is downloaded successfully ---------------------------\n")
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
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- ZIP file is not downloaded successfully ---------------------------\n\n")
#         assert False
