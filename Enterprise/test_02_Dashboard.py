import pytest
import requests
from _datetime import datetime
import globalvariables as globalvar
import test_GETutils as Utils
import Executor as Execute


def DashboardURL(activationCode, productActivationCode):
    return "enterprise/rest/dashboard/{activationCode}/{productActivationCode}".format(activationCode=activationCode,
                                                                                       productActivationCode=productActivationCode)

def DashboardRecentActivity(activationCode, productActivationCode, page, limit, start, end):
    return "enterprise/rest/auditlogs/{activationCode}/{productActivationCode}?page={page}&limit={limit}&start={start}&end={end}".format(
        activationCode=activationCode, productActivationCode=productActivationCode, page=page, limit=limit, start=start, end=end)

def DashboardCalls(activationCode, productActivationCode):
    return "enterprise/rest/dashboard/calls/{activationCode}/{productActivationCode}".format(
        activationCode=activationCode, productActivationCode=productActivationCode)


# GET Dashboard API
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_2001_Dashboard == 0, reason="Dashboard API is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.dashboard
@pytest.mark.run(order=20001)
def test_tc_2001_Dashboard_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        
        apiUrl = globalvar.BaseURL + DashboardURL(globalvar.activationCode, globalvar.productActivationCode)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
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
            print("\n" + "400 Bad Request!" + "\n")
            print("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            print("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            print("\n" + "500 Result not found!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print("\n\n--------------------------- FAIL to GET Dashboard Details ---------------------------\n\n")
        assert False

# WeTalk Call Info in Dashboard Page
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_2002_DashboardCalls == 0,
                    reason="WeTalk Call Info in Dashboard Page")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.dashboard
@pytest.mark.run(order=20002)
def test_tc_2002_Dashboard_Calls_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        apiURL = globalvar.BaseURL + DashboardCalls(globalvar.activationCode, globalvar.productActivationCode)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiURL, headers=Headers, timeout=globalvar.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
                  "\n" + "Request URL: " + apiURL +
                  "\n" + "Request Method: " + res.request.method +
                  "\n" + "Status Code: " + str(res.status_code) +
                  "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!" + "\n")
            print("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            print("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            print("\n" + "500 Result not found!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print("\n\n--------------------------- FAIL to GET Dashboard Calls ---------------------------\n\n")
        assert False


# Recent Activity in Dashboard
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_2003_DashboardRecentActivity == 0, reason="Recent Activity Logs in Dashboard is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.dashboard
@pytest.mark.run(order=20003)
def test_tc_2003_Dashboard_Recent_Activity_Logs_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        apiURL = globalvar.BaseURL + DashboardRecentActivity(globalvar.activationCode, globalvar.productActivationCode, globalvar.page_1, globalvar.page_500, globalvar.OneWeekCustomISO, globalvar.isoend)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiURL, headers=Headers, timeout=globalvar.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
                  "\n" + "Request URL: " + apiURL +
                  "\n" + "Request Method: " + res.request.method +
                  "\n" + "Status Code: " + str(res.status_code) +
                  "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!" + "\n")
            print("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            print("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            print("\n" + "500 Result not found!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print("\n\n--------------------------- FAIL to GET Dashboard Recent Activity Logs ---------------------------\n\n")
        assert False
