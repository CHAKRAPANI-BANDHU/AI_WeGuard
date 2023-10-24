from datetime import datetime
import pytest
import requests
import Executor as Execute
import globalvariables as globalvar
import test_GETutils as Utils
from Enterprise.test_08_Reports import test_tc_8003_Reports_Windows_Profiles_GET


def Overview(accountId):
    WeShieldOverview = "windows/rest/weshield/overview/account/{accountId}".format(accountId=accountId)
    return WeShieldOverview


def WeShieldAccountStatus(accountId, start, end, page, size):
    WeShieldStatus = "windows/rest/weshield/status/account/{accountId}?start={start}&end={end}&page={page}&size={size}".format(
        accountId=accountId, start=start, end=end, page=page, size=size)
    return WeShieldStatus


def ManualWeShieldScan(deviceId):
    WeShieldDeviceScan = "windows/rest/weshield/device/{deviceId}".format(deviceId=deviceId)
    return WeShieldDeviceScan


def WeShieldAccountHistory(accountId, start, end, page, size):
    HistoryWeShield = "windows/rest/weshield/history/account/64cb86dd80f4b80b1dc65e73?start=1695533848664&end=1698125848665&page=1&size=100".format(
        accountId=accountId, start=start, end=end, page=page, size=size)
    return HistoryWeShield

def WeShieldThreats(ids):
    Threats = "windows/rest/weshield/threat/status?ids=&searchString=".format(ids=ids)
    return Threats

# POST -- WeShield -- Overview
@pytest.mark.parametrize('url', [""])
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
        Payload = {"endDate": globalvar.end_timestamp, "startDate": globalvar.start_timestamp}
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


# Windows All Policies
def test_tc_19002_Windows_Policies_All():
    test_tc_8003_Reports_Windows_Profiles_GET()


# POST -- WeShield -- Status Account
@pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_19003_WeShield_Status_Account == 0,
                    reason="POST - WeShield Status Account is skipped")
@pytest.mark.usualtest
@pytest.mark.weshield
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=19003)
def test_tc_19003_WeShield_Status_Account_POST(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test.")
    try:
        apiUrl = globalvar.BaseURL + WeShieldAccountStatus(globalvar.accountId, globalvar.start_timestamp,
                                                            globalvar.month_timestamp, Page, Size)
        Headers = {'Authorization': 'Bearer ' + globalvar.bearerToken}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
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
            # Parse the API response
            response_data = res.json()
            if "entity" in response_data and "list" in response_data["entity"]:
                for item in response_data["entity"]["list"]:
                    ids = item.get("ids", [])  # Get the "ids" field, default to an empty list if it's missing
                    if ids:
                        print("IDs in the response:")
                        for id_value in ids:
                            print(id_value)
                            globalvar.WeShieldStatusIDs.append(id_value)
                    else:
                        print("No IDs in the response.")
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
        print(
            "------------------- GET -- WeShield - Failed to display the history of the scan results ---------------------------\n\n")
        assert False


# POST -- WeShield -- Manual Scan for a device
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_19004_WeShield_Manual_Scan_for_a_Device == 0,
                    reason="POST - WeShield Manual Scan to a device is skipped")
@pytest.mark.usualtest
@pytest.mark.weshield
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=19004)
def test_tc_19004_WeShield_ManualScan_Device_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test.")
    try:
        for deviceId in globalvar.Windows_DeviceIDs:
            apiUrl = globalvar.BaseURL + ManualWeShieldScan(deviceId)
            Headers = {'Authorization': 'Bearer ' + globalvar.bearerToken}
            res = requests.post(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
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
        print(
            "------------------- POST -- WeShield - Failed to initiate the manual scan to a device ---------------------------\n\n")
        assert False


# POST -- WeShield -- History Account
@pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_19005_WeShield_History_Account == 0,
                    reason="POST - WeShield History Account is skipped")
@pytest.mark.usualtest
@pytest.mark.weshield
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=19005)
def test_tc_19004_WeShield_Account_History_POST(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test.")
    try:
        apiUrl = globalvar.BaseURL + WeShieldAccountHistory(globalvar.accountId, globalvar.start_timestamp,
                                                            globalvar.month_timestamp, Page, Size)
        Headers = {'Authorization': 'Bearer ' + globalvar.bearerToken}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
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
        print(
            "------------------- POST -- WeShield - Failed to display the history of the scan results ---------------------------\n\n")
        assert False

# POST -- WeShield -- Threats
@pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_19006_WeShield_Threats_Detected_On_Devices == 0,
                    reason="POST - WeShield Threats detected on devices is skipped")
@pytest.mark.usualtest
@pytest.mark.weshield
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=19006)
def test_tc_19006_WeShield_Threats_GET(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test.")
    try:
        apiUrl = globalvar.BaseURL + WeShieldThreats(globalvar.WeShieldStatusIDs)
        Headers = {'Authorization': 'Bearer ' + globalvar.bearerToken}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
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
        print(
            "------------------- GET -- WeShield - Failed to get display the threats ---------------------------\n\n")
        assert False
