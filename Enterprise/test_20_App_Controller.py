from datetime import datetime

import pytest
import requests
import Executor as Execute
import globalvariables as globalvar
import test_GETutils as Utils

EnterpriseServerVersionURL = "enterprise/app/version"


# GET method to get notification server version
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_1111111_Enterprise_Server_Version_GET == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=1111111)
def test_tc_1111111_GET_Enterprise_Server_Version(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token, Skipping test")
    try:
        apiUrl = globalvar.BaseURL + EnterpriseServerVersionURL
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print(#"\n" + "Header: " + str(res.headers) + "\n"
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
            print("\n" + "500 Internal Server Error!")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, f"Received {res.status_code} response"
    except Exception as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        assert False, f"An exception occurred: {e}"
