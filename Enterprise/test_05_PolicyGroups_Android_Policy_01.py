import json
from datetime import datetime

import pytest
import requests
import Executor as Execute
import globalvariables as Globalinfo
import test_GETutils as Utils


def AndroidPolicy(policyId):
    GETAndroidPolicy = "enterprise/rest/weguard-v2/policy/{policyId}".format(policyId=policyId)
    return GETAndroidPolicy


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_4001_GET_Android_Policy_By_ID == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=400001)
def test_tc_4001_Android_Policy_By_ID_GET(url):
    now1 = datetime.now()
    if Globalinfo.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for policyId in Globalinfo.Android_Policy_IDs:
            apiUrl = Globalinfo.BaseURL + AndroidPolicy(policyId)
            Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
            res = requests.get(url=apiUrl, headers=Headers)
            if res.status_code == 200:
                print("\n" + "200 The request was a success!" + "\n")
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print(  # "\n" + "Header: " + str(res.headers) + "\n"
                    "\n" + "Request URL: " + apiUrl +
                    "\n" + "Request Method: " + res.request.method +
                    "\n" + "Status Code: " + str(res.status_code) +
                    "\n" + "Response: " + str(res.content) + "\n\n")
                Globalinfo.Android_Policy_Name = json.loads(res.content)['entity']['name']
                print("\nPolicy Name:" + Globalinfo.Android_Policy_Name + "\n")
            elif res.status_code == 400:
                print("\n" + "400 Bad Request!" + "\n")
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n" + "404 Result not found!" + "\n")
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n" + "500 Internal Server Error!" + "\n")
                assert False, "Received 500 response"
            else:
                print("Request did not succeed! Status code:", res.status_code)
                assert False, f"Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print("------------------- GET Android Policy Failed ---------------------------\n\n")
        assert False
