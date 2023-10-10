import json
from datetime import datetime
import pytest
import requests
import Executor as Execute
import globalvariables as Globalinfo
import test_GETutils as Utils

def AndroidDataUsage(page, size, type):
    GETDataUsage = "enterprise/rest/app/datausage?page={page}&size={size}&type={type}".format(page=page, size=size, type=type)
    return GETDataUsage

Types = ["MOBILE", "WIFI"]
Pages = [1, 2, 3, 4]
Sizes = [100, 300, 500, 700, 900, 1000]

# GET -- Data Usage for Mobile/Network
@pytest.mark.parametrize('Type, Page, Size', [(t, p, s) for t in Types for p in Pages for s in Sizes])
@pytest.mark.skipif(Execute.test_tc_11001_GET_Android_DataUsageOn == 0, reason="GET - Android Data Usage")
@pytest.mark.usualtest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=110001)
def test_tc_11001_GET_Android_Data_Usage_On(Type, Page, Size):
    now1 = datetime.now()
    if Globalinfo.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test.")
    try:
        apiUrl = Globalinfo.BaseURL + AndroidDataUsage(Page, Size, Type)
        headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
        res = requests.get(url=apiUrl, headers=headers)
        if res.status_code == 200:
            print("\n200 The request was a success!\n")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(
                "\nRequest URL: " + apiUrl +
                "\nRequest Method: " + res.request.method +
                "\nStatus Code: " + str(res.status_code) +
                "\nResponse: " + str(res.content) + "\n\n"
            )
        elif res.status_code == 400:
            print("\n400 Bad Request!\n")
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n404 Result not found!\n")
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n500 Internal Server Error!\n")
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, f"Received {res.status_code} response"
    except Exception as e:
        print("Exception: " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print("------------------- Failed - GET Android Data Usage on left navigation bar ---------------------------\n\n")
        assert False
