from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import WeGuardLogger as WeGuard
import general_payload as GeneralPayload

def WindowsDevice(WindowsMongoDBID):
    return "windows/rest/device/{WindowsMongoDBID}".format(WindowsMongoDBID=WindowsMongoDBID)

def WindowsDeviceDetails(end, page, policyId, size, start):
    return "windows/rest/device/all?end={end}&page={page}&policyId={policyId}&size={size}&start={start}".format(end=end, page=page, policyId=policyId, size=size, start=start)

def WindowsDevicesByPolicyIDs(page, size):
    return "windows/rest/device/bulk?page={page}&size={size}".format(page=page, size=size)

def WindowsDeviceCommand(WindowsMongoDBID):
    return "windows/rest/device/command/{WindowsMongoDBID}".format(WindowsMongoDBID=WindowsMongoDBID)

# GET method to get Windows devices by Mongo DB ID
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0000001_Windows_DeviceDetailsByMongoID_GET == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=100001)
def test_tc_0000001_Windows_Device_Details_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
      for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
        WindowsDevices = WindowsDevice(mongodbId)
        apiUrl = globalvar.BaseURL + WindowsDevices
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            WeGuard.logger.debug(curl_str1)
            WeGuard.logger.debug("\n" + "200 The request was a success!")
            WeGuard.logger.debug("\n" + "Header: " + str(res.headers) +
                                 "\n" + "Request URL: " + apiUrl +
                                 "\n" + "Request Method: " + res.request.method +
                                 "\n" + "Status Code: " + str(res.status_code) +
                                 "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            WeGuard.logger.error("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            WeGuard.logger.error("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            WeGuard.logger.error("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            WeGuard.logger.error("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("-------------------------- Failed to display the Windows device details by Mongo DB ID ---------------------------\n\n")
        assert False

# PUT method to update the tags for Windows devices by Mongo DB ID
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0000002_Windows_Device_Updates_Tags_By_MongoID_PUT == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=100002)
def test_tc_0000002_Windows_Device_Updates_Tags_By_MongoID_PUT(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
      for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
        WindowsDevices = WindowsDevice(mongodbId)
        apiUrl = globalvar.BaseURL + WindowsDevices
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.put(url=apiUrl, headers=Headers, json=GeneralPayload.PUT_UpdateTags_Windows_Device, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            WeGuard.logger.debug(curl_str1)
            WeGuard.logger.debug("\n" + "200 The request was a success!")
            WeGuard.logger.debug("\n" + "Header: " + str(res.headers) +
                                 "\n" + "Request URL: " + apiUrl +
                                 "\n" + "Request Method: " + res.request.method +
                                 "\n" + "Status Code: " + str(res.status_code) +
                                 "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            WeGuard.logger.error("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            WeGuard.logger.error("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            WeGuard.logger.error("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            WeGuard.logger.error("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("-------------------------- Failed to update the tags for the Windows devices by Mongo DB ID ---------------------------\n\n")
        assert False

# GET method to fetch device details by policy id
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0000003_Windows_Fetch_Device_Details_GET == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=100003)
def test_tc_0000003_Windows_Fetch_Device_Details_GET(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
      for policy_id in globalvar.Windows_profile_ids:
        WindowsDevices = WindowsDeviceDetails(globalvar.isoend, globalvar.page_1, policy_id, globalvar.page_1000, globalvar.isostart)
        apiUrl = globalvar.BaseURL + WindowsDevices
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            WeGuard.logger.debug(curl_str1)
            WeGuard.logger.debug("\n" + "200 The request was a success!")
            WeGuard.logger.debug("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            WeGuard.logger.error("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            WeGuard.logger.error("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            WeGuard.logger.error("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            WeGuard.logger.error("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("-------------------------- Failed to fetch Windows device details by policy id ---------------------------\n\n")
        assert False

# POST method to fetch devices by PolicyIds
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0000004_Windows_Fetch_Devices_By_PolicyIDs_POST == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=100004)
def test_tc_0000004_Windows_Fetch_Devices_By_PolicyIDs_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
      for policy_id in globalvar.Windows_profile_ids:
        WindowsDevices = WindowsDevicesByPolicyIDs(globalvar.page_1, globalvar.page_1000)
        apiUrl = globalvar.BaseURL + WindowsDevices
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {"policyIds": [policy_id]}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            WeGuard.logger.debug(curl_str1)
            WeGuard.logger.debug("\n" + "200 The request was a success!")
            WeGuard.logger.debug("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            WeGuard.logger.error("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            WeGuard.logger.error("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            WeGuard.logger.error("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            WeGuard.logger.error("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("-------------------------- Failed to fetch Windows device details by policy id ---------------------------\n\n")
        assert False

# POST method to add commands
# Restart of a device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0000005_Windows_Add_Device_Commands_POST == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=100005)
def test_tc_0000005_Windows_Add_Device_Commands_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
      for mongodbId in globalvar.Windows_Mongo_DB_DeviceIDs:
        apiUrl = globalvar.BaseURL + WindowsDeviceCommand(mongodbId)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {"command": "RebootNow"}
        # For Wipe: RemoteWipe & type
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            WeGuard.logger.debug(curl_str1)
            WeGuard.logger.debug("\n" + "200 The request was a success!")
            WeGuard.logger.debug("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
        elif res.status_code == 400:
            WeGuard.logger.error("\n" + "400 Bad Request!" + "\n")
            # Add your assertions or actions for 400 Bad Request response here
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            WeGuard.logger.error("\n" + "404 Result not found!" + "\n")
            # Add your assertions or actions for 404 Not Found response here
            assert False, "Received 404 response"
        elif res.status_code == 500:
            WeGuard.logger.error("\n" + "500 Internal Server Error!" + "\n")
            # Add your assertions or actions for 500 Internal Server Error response here
            assert False, "Received 500 response"
        else:
            WeGuard.logger.error("Request did not succeed! Status code:", res.status_code)
            assert False, "Received {res.status_code} response"
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("-------------------------- Failed to execute the device command ---------------------------\n\n")
        assert False
