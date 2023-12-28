import json
from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils


POSTDeviceFilters = "enterprise/rest/v3/device/filters"

def GETApplicationFilters():
    return "enterprise/rest/weguard-v2/license/application/filters".format()

def POSTAppUsageStatsAll():
    return "enterprise/rest/app-usage/stats/all".format()

# Screen Time
# POST method to get all devices screen time details after clicking on the Screen Time on left navigation bar
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_20001_ScreenTime_DeviceFilters_POST == 0,
                    reason="Screen Time - Device Filters is skipped")
@pytest.mark.poitivetest
@pytest.mark.screentime
@pytest.mark.regressiontest
@pytest.mark.run(order=200001)
def test_tc_200001_ScreenTime_POST_DeviceFilters(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + POSTDeviceFilters
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        DeviceFiltersPOST = {"tag6": None, "tag7": None, "tag8": None}
        res = requests.post(url=apiUrl, headers=Headers, json=DeviceFiltersPOST,
                            timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(DeviceFiltersPOST) +
                "\n" + "Response: " + str(res.content) + "\n")
            # Check if "regions" key is present in the JSON response
            json_response = json.loads(res.content)
            if 'regions' in json_response and json_response['regions']:
                globalvar.Regions = json_response['regions']
                print("Regions are present: " + str(globalvar.Regions))
                
            else:
                print("No regions available in the response.")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the screen time details for the devices ---------------------------\n\n")
        assert False
        
# GET method to get/retrieve the applications filters
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_20002_ScreenTime_ApplicationsFilters_GET == 0,
                    reason="Screen Time - Applications Filters is skipped")
@pytest.mark.poitivetest
@pytest.mark.screentime
@pytest.mark.regressiontest
@pytest.mark.run(order=200002)
def test_tc_200002_ScreenTime_GET_ApplicationsFilters(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + GETApplicationFilters()
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the applications in screen time page ---------------------------\n\n")
        assert False
        
# All App Usage Stats POST method
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_20003_ScreenTime_AppUsageStats_POST == 0,
                    reason="Screen Time - App Usage Stats is skipped")
@pytest.mark.poitivetest
@pytest.mark.screentime
@pytest.mark.regressiontest
@pytest.mark.run(order=200003)
def test_tc_200003_ScreenTime_POST_AppUsageStats(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + POSTAppUsageStatsAll()
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=globalvar.AllAppUsageStats,
                            timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(
            "------------- Failed to display the applications in screen time page ---------------------------\n\n")
        assert False