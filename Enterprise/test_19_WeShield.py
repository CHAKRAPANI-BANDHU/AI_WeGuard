from datetime import datetime
import pytest
import requests
import Executor as Execute
import globalvariables as globalvar
import test_GETutils as Utils


def Overview(accountId):
    WeShieldOverview = "windows/rest/weshield/overview/account/{accountId}".format(accountId=accountId)
    return WeShieldOverview

# POST -- WeShield -- Overview
@pytest.mark.parametrize('url', [])
@pytest.mark.skipif(Execute.test_tc_19001_WeShield_Overview == 0, reason="POST - WeShield Overview is skipped")
@pytest.mark.usualtest
@pytest.mark.weshield
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=19001)
def test_tc_19001_WeShield_Overview_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test.")
    try:
        apiUrl = globalvar.BaseURL + Overview(globalvar.accountId)
        Headers = {'Authorization': 'Bearer ' + globalvar.bearerToken}
        Payload = {"startDate": globalvar.start_timestamp, "endDate": globalvar.end_timestamp}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
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
        print("------------------- POST -- Failed to see WeShield - Overview ---------------------------\n\n")
        assert False
