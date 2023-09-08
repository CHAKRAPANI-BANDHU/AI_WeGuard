import json
from datetime import datetime

import pytest
import requests

import Executor as Execute
import Logs as WeGuard
import globalvariables as globalvar
import jsonnames
import general_payload as requestdata
import test_GETutils as Utils

# URLs
LoginURL = "enterprise/rest/users/login"
event_Login = "enterprise/rest/weguard/logs/events"


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0001_Login == 0, reason="Enterprise is compulsory")
@pytest.mark.positivetest
@pytest.mark.login
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.raretest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10000)
def test_tc_0001_Login(url):
    now1 = datetime.now()
    try:
        apiUrl = globalvar.BaseURL + LoginURL
        jsonData = {
            jsonnames.USERNAME: globalvar.userName,
            jsonnames.PASSWORD: globalvar.password
        }
        res = requests.post(url=apiUrl, json=jsonData, timeout=globalvar.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        jsonData_str = str(jsonData)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
                  "\n" + "Request URL: " + apiUrl +
                  "\n" + "Request Method: " + res.request.method +
                  "\n" + "Status Code: " + str(res.status_code) +
                  "\n" + "Request Payload: " + jsonData_str +
                  "\n" + "Response: " + str(res.content) + "\n")
            # print(json.loads(res.content)['entity']['userData'])
            globalvar.bearerToken = json.loads(res.content)['entity']['jwtToken']
            globalvar.activationCode = json.loads(res.content)['entity']['activationCode']
            globalvar.productActivationCode = json.loads(res.content)['entity']['productActivationCode']
            globalvar.fname = json.loads(res.content)['entity']['fName']
            globalvar.lname = json.loads(res.content)['entity']['lName']
            globalvar.accountId = json.loads(res.content)['entity']['userData'].get('accountId')
            globalvar.name = globalvar.fname + "%20%20" + globalvar.lname
            globalvar.companyName = json.loads(res.content)['entity']['companyName']
            globalvar.enterpriseId = json.loads(res.content)['entity']['enterpriseId']
            assert globalvar.userName == json.loads(res.content)['entity']['userName']
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "500 Result not found!")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.positivetest
@pytest.mark.login
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.usualtest
@pytest.mark.skipif(Execute.test_tc_0002_Login_Event == 0, reason="test is skipped")
@pytest.mark.run(order=10001)
def test_tc_0002_Login_Event(url):
    now1 = datetime.now()
    try:
        apiUrl = globalvar.BaseURL + event_Login
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=requestdata.login_event, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "500 Result not found!")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("--------------------------- Failed Enterprise Events ---------------------------\n\n")
        assert False

# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_000003_AccountAdmin_Invalid_email == 0, reason="test is skipped")
# @pytest.mark.login
# @pytest.mark.negativetest
# @pytest.mark.run(order=10003)
# def test_tc_000002_InvalidEmail(url):
#     now1 = datetime.now()
#     try:
#         apiUrl = globalvar.BaseURL + globalvar.LoginURL
#         jsonData = {
#             jsonnames.USERNAME: "chakrapani078@gmail.com",
#             jsonnames.PASSWORD: globalvar.password
#         }
#         res = requests.post(url=apiUrl, json=jsonData, timeout=globalvar.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#             print("\n" + "Header: " + str(res.headers) +
#                                  "\n" "Request URL: " + apiUrl +
#                                  "\n" + "Request Method: " + res.request.method +
#                                  "\n" + "Status Code: " + str(res.status_code) +
#                                  "\n" + "Response: " + str(res.content) + "\n")
#             print("JWT token is :" + globalvar.bearerToken)
#             assert globalvar.userName == json.loads(res.content)['entity']['userName']
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
#     except requests.RequestException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
#         assert False, f"An exception occurred: {e}"
#
#
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_000004_AccountAdmin_Invalid_password == 0, reason="test is skipped")
# @pytest.mark.login
# @pytest.mark.usualtest
# @pytest.mark.negativetest
# @pytest.mark.run(order=10004)
# def test_tc_000003_InvalidPassword(url):
#     now1 = datetime.now()
#     try:
#         apiUrl = globalvar.BaseURL + globalvar.LoginURL
#         jsonData = {
#             jsonnames.USERNAME: globalvar.userName,
#             jsonnames.PASSWORD: "Password@123"
#         }
#         res = requests.post(url=apiUrl, json=jsonData, timeout=globalvar.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         if res.status_code == 200:
#             print("\n" + "200 The request was a success!")
#            print("\n" + "Header: " + str(res.headers) +
#                      "\n" + "Request URL: " + apiUrl +
#                      "\n" + "Request Method: " + res.request.method +
#                      "\n" + "Status Code: " + str(res.status_code) +
#                      "\n" + "Response: " + str(res.content) + "\n")
#             print("JWT token is :" + globalvar.bearerToken)
#             assert globalvar.userName == json.loads(res.content)['entity']['userName']
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
#     except requests.RequestException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
#         assert False, f"An exception occurred: {e}"
