# from datetime import datetime
# import pytest
# import requests
# import Executor as Execute
# import globalvariables as Globalinfo
# import test_GETutils as Utils
#
#
# def License(pageSize, page):
#     GETLicense = "enterprise/rest/weguard-v2/license?pageSize={pageSize}&page={page}".format(pageSize=pageSize,
#                                                                                              page=page)
#     return GETLicense
#
#
# def AppleProfiles(page, size):
#     GETAppleProfiles = "apple/rest/profile/all?page={page}&size={size}".format(page=page, size=size)
#     return GETAppleProfiles
#
#
# WindowsProfiles = "windows/rest/policy/all"
#
#
# # GET -- Reports -- License
# @pytest.mark.parametrize('Page, Size', [(p, s) for p in Globalinfo.page for s in Globalinfo.pageSize])
# @pytest.mark.skipif(Execute.test_tc_8001_GET_Reports_License == 0, reason="GET - License in Reports")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=800001)
# def test_tc_8001_Reports_License_GET(Page, Size):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test.")
#     try:
#         apiUrl = Globalinfo.BaseURL + License(Page, Size)
#         headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#         res = requests.get(url=apiUrl, headers=headers)
#         if res.status_code == 200:
#             print("\n200 The request was a success!\n")
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print(
#                 "\nRequest URL: " + apiUrl +
#                 "\nRequest Method: " + res.request.method +
#                 "\nStatus Code: " + str(res.status_code) +
#                 "\nResponse: " + str(res.content) + "\n\n"
#             )
#         elif res.status_code == 400:
#             print("\n400 Bad Request!\n")
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n404 Result not found!\n")
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n500 Internal Server Error!\n")
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- Failed - GET License ---------------------------\n\n")
#         assert False
#
#
# # GET -- Reports -- Apple Profiles
# @pytest.mark.parametrize('Page, Size', [(p, s) for p in Globalinfo.page for s in Globalinfo.pageSize])
# @pytest.mark.skipif(Execute.test_tc_8002_GET_Reports_Apple_Profiles == 0, reason="GET - Apple Profiles in Reports")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=800002)
# def test_tc_8002_Reports_Apple_Profiles_GET(Page, Size):
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test.")
#     try:
#         apiUrl = Globalinfo.BaseURL + AppleProfiles(Page, Size)
#         headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#         res = requests.get(url=apiUrl, headers=headers)
#         if res.status_code == 200:
#             print("\n200 The request was a success!\n")
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print(
#                 "\nRequest URL: " + apiUrl +
#                 "\nRequest Method: " + res.request.method +
#                 "\nStatus Code: " + str(res.status_code) +
#                 "\nResponse: " + str(res.content) + "\n\n"
#             )
#         elif res.status_code == 400:
#             print("\n400 Bad Request!\n")
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n404 Result not found!\n")
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n500 Internal Server Error!\n")
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- Failed - GET Apple Profiles ---------------------------\n\n")
#         assert False
#
#
# # GET -- Reports -- Windows Profiles
# @pytest.mark.skipif(Execute.test_tc_8003_GET_Reports_Windows_Profiles == 0, reason="GET - Windows Profiles in Reports")
# @pytest.mark.usualtest
# @pytest.mark.policygroups
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.positivetest
# @pytest.mark.run(order=800003)
# def test_tc_8003_Reports_Windows_Profiles_GET():
#     now1 = datetime.now()
#     if Globalinfo.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test.")
#     try:
#         apiUrl = Globalinfo.BaseURL + WindowsProfiles
#         headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
#         res = requests.get(url=apiUrl, headers=headers)
#         if res.status_code == 200:
#             print("\n200 The request was a success!\n")
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print(
#                 "\nRequest URL: " + apiUrl +
#                 "\nRequest Method: " + res.request.method +
#                 "\nStatus Code: " + str(res.status_code) +
#                 "\nResponse: " + str(res.content) + "\n\n"
#             )
#         elif res.status_code == 400:
#             print("\n400 Bad Request!\n")
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n404 Result not found!\n")
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n500 Internal Server Error!\n")
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("Exception: " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------------- Failed - GET Windows Profiles ---------------------------\n\n")
#         assert False
