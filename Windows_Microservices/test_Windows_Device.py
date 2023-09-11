from datetime import datetime

import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import WeGuardLogger as WeGuard

def DeviceDetailsByMongoID(WindowsMongoDBID):
    return "windows/rest/device/{WindowsMongoDBID}".format(WindowsMongoDBID=WindowsMongoDBID)

# Windows Devices
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0000001_Windows_DeviceDetailsByMongoID == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.devices
@pytest.mark.regressiontest
@pytest.mark.run(order=100000)
def test_tc_0000001_Windows_Device_Details_View(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
      for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
        WindowsDevices = DeviceDetailsByMongoID(mongodbId)
        apiUrl = globalvar.BaseURL + WindowsDevices
        print(globalvar.Windows_Mongo_DB_DeviceIDs)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
                WeGuard.logger.debug("\n" + "200 The request was a success!")
                WeGuard.logger.debug("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
                WeGuard.logger.debug("-------------------------- Windows device details is displayed by Mongo DB ID ---------------------------\n\n")
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
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        print("-------------------------- Failed to display the Windows device details by Mongo DB ID ---------------------------\n\n")
        WeGuard.logger.error("-------------------------- Failed to display the Windows device details by Mongo DB ID ---------------------------\n\n")
        assert False
        