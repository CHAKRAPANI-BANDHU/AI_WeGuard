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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalcheck.BaseURL + config
#         Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.SharedFolderconfigwithoutSign,
#                             timeout=globalcheck.timeout)
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
#                 "\n\n--------------------------- Shared Folders WeBox upload config without sign passed  ---------------------------")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalcheck.BaseURL + config
#         Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#         WeBox.SharedFolderconfigwithSign["activationCode"] = globalcheck.activationCode
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.SharedFolderconfigwithSign,
#                             timeout=globalcheck.timeout)
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
#                 "\n\n--------------------------- Shared Folders WeBox upload config with sign passed ---------------------------")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for name in WeBox.sharedfolderslist:
#             viewfoldersinsharedfolder = url_formatter8(name, globalcheck.page_1, globalcheck.page_100, WeBox.isostart,
#                                                        WeBox.isoend)
#             apiUrl = globalcheck.BaseURL + viewfoldersinsharedfolder
#             Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#             res = requests.get(url=apiUrl, headers=Headers, timeout=globalcheck.timeout)
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
#                     "\n\n--------------------------- Files are available in globals shared folder ---------------------------")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "500 Result not found!")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalcheck.Android_profile_ids:
#             for name in WeBox.policyfolderslist:
#                 viewfilesinpolicyfolders = url_formatter9(policyId, name, globalcheck.page_1, globalcheck.page_100,
#                                                           WeBox.isostart, WeBox.isoend)
#                 # viewfilesinpolicyfolders = url_formatter9(globalcheck.Android_profile_ids, 'AI Documents', globalcheck.page_1, globalcheck.page_100, WeBox.isostart, WeBox.isoend)
#                 apiUrl = globalcheck.BaseURL + viewfilesinpolicyfolders
#                 Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#                 res = requests.get(url=apiUrl, headers=Headers, timeout=globalcheck.timeout)
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
#                         "\n\n--------------------------- Files are available in policy groups folder ---------------------------")
#                 elif res.status_code == 400:
#                     print("\n" + "400 Bad Request!")
#                     # Add your assertions or actions for 400 Bad Request response here
#                     assert False, "Received 400 Bad Request response"
#                 elif res.status_code == 404:
#                     print("\n" + "500 Result not found!")
#                     # Add your assertions or actions for 404 Not Found response here
#                     assert False, "Received 404 response"
#                 elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         sharedgroupfiles = url_formatter10(globalcheck.activationCode, globalcheck.page_1, globalcheck.page_100)
#         apiUrl = globalcheck.BaseURL + sharedgroupfiles
#         Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalcheck.timeout)
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
#                 "\n\n--------------------------- Folder names are available upon clicking on clear in shared folders ---------------------------")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         for policyId in globalcheck.Android_profile_ids:
#             for name in WeBox.policyfolderslist:
#                 policygroupfiles = url_formatter11(policyId, name, globalcheck.page_1, globalcheck.page_100)
#                 # policygroupfiles = url_formatter11(globalcheck.Android_profile_ids, 'AI Documents', globalcheck.page_1, globalcheck.page_100)
#                 apiUrl = globalcheck.BaseURL + policygroupfiles
#                 Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#                 res = requests.get(url=apiUrl, headers=Headers, timeout=globalcheck.timeout)
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
#                         "\n\n--------------------------- Files are available upon clicking on clear in policy group folders ---------------------------")
#                 elif res.status_code == 400:
#                     print("\n" + "400 Bad Request!")
#                     # Add your assertions or actions for 400 Bad Request response here
#                     assert False, "Received 400 Bad Request response"
#                 elif res.status_code == 404:
#                     print("\n" + "500 Result not found!")
#                     # Add your assertions or actions for 404 Not Found response here
#                     assert False, "Received 404 response"
#                 elif res.status_code == 500:
#                     print("\n" + "500 Internal Server Error!")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         sharedgroupconfig = url_formatter12(globalcheck.activationCode, globalcheck.productActivationCode)
#         apiUrl = globalcheck.BaseURL + sharedgroupconfig
#         Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalcheck.timeout)
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
#                 "\n\n--------------------------- Get the configs of Shared Folders Pass ---------------------------")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         pdf = 'uploader/download/pdf'
#         apiUrl = globalcheck.BaseURL + pdf
#         # compact_obj = json.dumps(WeBox.pdf)
#         Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.pdf, timeout=globalcheck.timeout)
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
#                 "\n\n--------------------------- PDF file is downloaded successfully ---------------------------")
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
#     if globalcheck.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         zip = 'uploader/download/zip'
#         apiUrl = globalcheck.BaseURL + zip
#         # testing = jsonpickle.encode(WeBox.zip)
#         Headers = {'Authorization': 'Bearer {}'.format(globalcheck.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=WeBox.zip, timeout=globalcheck.timeout)
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
#                 "\n\n--------------------------- ZIP file is downloaded successfully ---------------------------")
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
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error(
#             "\n\n--------------------------- ZIP file is not downloaded successfully ---------------------------\n\n")
#         assert False
