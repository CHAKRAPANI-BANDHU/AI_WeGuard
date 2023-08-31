from datetime import datetime
from itertools import product

import pytest
import requests
import Executor as Execute
import WeGuardlogger as WeGuard
import globalvariables 
import test_GETutils as Utils

def AlertTypeLevels(accountId, start, end, page, size, type, level):
    url4 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}&level={level}".format(
        accountId=accountId, start=start, end=end, page=page, size=size, type=type, level=level)
    return url4

def AlertTypes(accountId, start, end, page, size, type):
    url5 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}".format(
        accountId=accountId, start=start, end=end, page=page, size=size, type=type)
    return url5

def AlertsLevel(accountId, start, end, page, size, level):
    url6 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&level={level}".format(
        accountId=accountId, start=start, end=end, page=page, size=size, level=level)
    return url6

def AllAlerts(accountId, start, end, page, size):
    GETAccountLevelAlert = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}".format(
        accountId=accountId, start=start, end=end, page=page, size=size)
    return GETAccountLevelAlert


def url_formatter4(accountId, start, end, page, size, level, ack):
    url6 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&level={level}&ack={ack}".format(
        accountId=accountId, start=start, end=end, page=page, size=size, level=level, ack=ack)
    return url6


def url_formatter5(accountId):
    AcknowledgeAlerts = "notification/rest/alert/account/{accountId}/read".format(accountId=accountId)
    return AcknowledgeAlerts


# Define the list of alert types
Alert_Types = ["ALL", "BATTERY", "DATA_USAGE", "KIOSK_LOCKED", "KIOSK_UNLOCKED", "ADMIN_LOCKED", "DEVICE_REBOOTED",
               "DEVICE_SHUTDOWN", "DEVICE_WIPED", "DEVICE_DELETED", "ROOTED_ENROLL", "MEMORY_ALERT", "DISC_USAGE",
               "DEVICE_MARKED_REPLACED", "DEVICE_MARKED_LOST", "DEVICE_MARKED_STOLEN", "DEVICE_CONNECTED_BACK",
               "SIM_LOCK_CHANGED", "RESET_PASSWORD", "SIM_REMOVED", "SIM_CHANGED", "SIM_ADDED", "UNINSTALL_WEGUARD"]

# Define the list of alert level
Alert_Levels = ["ALL", "LOW", "WARNING", "CRITICAL", "IN_FENCE", "OUT_FENCE"]

# Create a list of all combinations of alert_type and alert_level
alert_combinations = list(product(Alert_Types, Alert_Levels))

# Alert Types
@pytest.mark.parametrize('alert_type', Alert_Types)
@pytest.mark.skipif(Execute.test_tc_1001_Alerts_Types_and_Levels_ALL == 0,
                    reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10431)
def test_Alert_Types(alert_type):
    now1 = datetime.now()
    if globalvariables.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        alert_url = AlertTypes(globalvariables.accountId, globalvariables.isostart, globalvariables.isoend,
                                   globalvariables.page_1, globalvariables.page_1000, alert_type)
        apiUrl = globalvariables.BaseURL + alert_url
        Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
                                 "\n" + "Request URL: " + apiUrl +
                                 "\n" + "Request Method: " + res.request.method +
                                 "\n" + "Status Code: " + str(res.status_code) +
                                 "\n" + "Response: " + str(res.content))
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
            assert False, f"Received {res.status_code} response"
        print(
            f"\n--------------------------- Alert notifications of type={alert_type} and level=All ---------------------------\n")
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error(
            f"\n--------------------------- Not available alert notifications of type={alert_type} and level=All ---------------------------\n")
        assert False

# Alert Levels
@pytest.mark.parametrize('alert_level', Alert_Levels)
@pytest.mark.skipif(Execute.test_tc_1002_Alerts_Levels == 0,
                    reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10432)
def test_Alert_Levels(alert_level):
    now1 = datetime.now()
    if globalvariables.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        alert_level = AlertsLevel(globalvariables.accountId, globalvariables.isostart, globalvariables.isoend,
                                   globalvariables.page_1, globalvariables.page_1000, alert_level)
        apiUrl = globalvariables.BaseURL + alert_level
        Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
                                 "\n" + "Request URL: " + apiUrl +
                                 "\n" + "Request Method: " + res.request.method +
                                 "\n" + "Status Code: " + str(res.status_code) +
                                 "\n" + "Response: " + str(res.content))
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
            assert False, f"Received {res.status_code} response"
        print(
            f"\n--------------------------- Alert notifications of type={alert_level} and level=All ---------------------------\n")
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        now2 = datetime.now()
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        WeGuard.logger.error(
            f"\n--------------------------- Not available alert notifications of type={alert_level} and level=All ---------------------------\n")
        assert False

# Alert Types and Levels
@pytest.mark.skipif(Execute.test_tc_1003_Alerts_Types_and_Levels == 0,
                    reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10433)
def test_Alert_Types_and_Levels():
    now1 = datetime.now()
    if globalvariables.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
        try:
            for alert_level in Alert_Levels:
                for alert_type in Alert_Types:
                    apiUrl = AlertTypeLevels(globalvariables.accountId, globalvariables.isostart,
                                             globalvariables.isoend, globalvariables.page_1, globalvariables.page_1000,
                                             alert_type, alert_level)
                    Headers = {'Authorization': 'Bearer {}'.format(globalvariables.bearerToken)}
                    res = requests.get(url=apiUrl, headers=Headers, timeout=globalvariables.timeout)
                    curl_str1 = Utils.getCurlEquivalent(res)
                    print(curl_str1)
                    print(
                        f"--------------------------- Alert notifications of type={alert_type} and level={alert_level} ---------------------------\n")
                    if res.status_code == 200:
                        print("\n" + "200 The request was a success!" + "\n")
                        print("\n" + "Header: " + str(res.headers) +
                              "\n" + "Request URL: " + apiUrl +
                              "\n" + "Request Method: " + res.request.method +
                              "\n" + "Status Code: " + str(res.status_code) +
                              "\n" + "Response: " + str(res.content))
                    elif res.status_code == 400:
                        print("\n400 Bad Request!")
                        assert False, "Received 400 Bad Request response"
                    elif res.status_code == 404:
                        print("\n404 Result not found!")
                        assert False, "Received 404 response"
                    elif res.status_code == 500:
                        print("\n500 Internal Server Error!")
                        assert False, "Received 500 response"
                    else:
                        print("Request did not succeed! Status code:", res.status_code)
                        assert False, f"Received {res.status_code} response"
        except BaseException as e:
            print("Exception:", str(e))
            now2 = datetime.now()
            print("Time taken:", now2 - now1)
            assert False