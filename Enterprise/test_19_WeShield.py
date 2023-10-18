# from datetime import datetime
# import pytest
# import requests
# import Executor as Execute
# import globalvariables as Globalinfo
# import test_GETutils as Utils
#
#
# def Overview(pageSize, page):
#     WeShieldOverview = "enterprise/rest/weguard-v2/license?pageSize={pageSize}&page={page}".format(pageSize=pageSize,
#                                                                                              page=page)
#     return WeShieldOverview
#
# # GET -- Reports -- License
# @pytest.mark.parametrize('url', [])
# @pytest.mark.skipif(Execute.test_tc_19001_WeShield_Overview == 0, reason="GET - WeShield Overview is skipped")
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