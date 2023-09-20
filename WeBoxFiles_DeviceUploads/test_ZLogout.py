# import pytest
# import requests
# from datetime import datetime
# import globalvariables as var
# import Logs as WeGuard
# import Executor as Execute
# import test_GETutils as Utils
# import payloads as information
#
# LogoutURL = 'enterprise/rest/weguard/logs/events'
#
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_1000_Logout == 0, reason="Logged out Successfully")
# @pytest.mark.raretest
# @pytest.mark.logout
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.run(order=10448)
# def test_tc_000001_Logout(url):
#     print("\n\n------------------- TC 000001 Logout Start ---------------------------\n")
#     now1 = datetime.now()
#     if var.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = var.BaseURL + LogoutURL
#         Headers = {'Authorization': 'Bearer {}'.format(var.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=information.logout, timeout=var.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print(#"\n" + "Header: " + str(res.headers) + "\n"
#                                  "\n" + "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
#             print("------------------- Logged out from the account ---------------------------\n\n")
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
#         print("------------------- Logout is failed ---------------------------\n\n")
#         assert False
#
