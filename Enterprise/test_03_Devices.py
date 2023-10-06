from datetime import datetime

import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import general_payload as RequestInfo


def allDevices(page, size):
    AllDevices = "enterprise/rest/v3/device/all?page={page}&size={size}".format(page=page, size=size)
    return AllDevices


def searchPolicies(page, size, search):
    searchPolicy = "enterprise/rest/v3/policy/all?page={page}&size={size}&search={search}&deviceCount=false".format(
        page=page, size=size, search=search)
    return searchPolicy


# Page Size = 100
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_3001_All_Devices_100 == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.devices
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=30001)
def test_tc_3001_All_Devices_100(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token  Skipping test")
    try:
        Devices_PageSize_100 = allDevices(globalvar.page_1, globalvar.page_100)
        apiUrl = globalvar.BaseURL + Devices_PageSize_100
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.AllDevices, timeout=globalvar.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print(
                # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n")
            json_resp = res.json()
            # Store devices based on platform and type
            for device in json_resp.get('list', []):
                platform = device.get('type')  # Use 'type' key to determine the platform
                mongoDBDeviceID = device.get('id')
                device_id = device.get('deviceId')
                # Check platform and store device IDs accordingly
                if platform == 'ANDROID':
                    globalvar.Android_Devices.append((mongoDBDeviceID, device_id))
                    globalvar.Android_DeviceIDs.append(device_id)
                    globalvar.Android_Mongo_DB_DeviceIDs.append(mongoDBDeviceID)
                elif platform == 'IOS':
                    globalvar.iOS_Devices.append((mongoDBDeviceID, device_id))
                    globalvar.iOS_DeviceIDs.append(device_id)
                    globalvar.iOS_Mongo_DB_DeviceIDs.append(mongoDBDeviceID)
                elif platform == 'WINDOWS':
                    globalvar.Windows_Devices.append((mongoDBDeviceID, device_id))
                    globalvar.Windows_DeviceIDs.append(device_id)
                    globalvar.Windows_Mongo_DB_DeviceIDs.append(mongoDBDeviceID)
                else:
                    print("\nInvalid platform type")

            # Display the extracted device IDs of Windows, Android and iOS.

            # Windows Devices Information
            if globalvar.Windows_Devices:
                print("\nWindows Devices Information:")
                for device in globalvar.Windows_Devices:
                    print("Windows Mongo DB Device ID:", device[0])
                    print("Windows Device ID:", device[1])
                print("\nExtracted Windows Devices Information")
                Windows_DeviceIDs_str = ', '.join(device[1] for device in globalvar.Windows_Devices)
                print("\nWindows Device IDs: " + Windows_DeviceIDs_str)
                Windows_MongoDBDeviceID_str = ', '.join(device[0] for device in globalvar.Windows_Devices)
                print("\nWindows Mongo DB Device IDs: " + Windows_MongoDBDeviceID_str)
            else:
                print("\nNo Windows Devices found.")

            # Android Devices Information
            if globalvar.Android_Devices:
                print("\nAndroid Devices Information:")
                for device in globalvar.Android_Devices:
                    print("Android Mongo DB Device ID:", device[0])
                    print("Android Device ID:", device[1])
                print("\nExtracted Android Devices Information")
                Android_DeviceIDs_str = ', '.join(device[1] for device in globalvar.Android_Devices)
                print("\nAndroid Device IDs: " + Android_DeviceIDs_str)
                Android_MongoDBDeviceID_str = ', '.join(device[0] for device in globalvar.Android_Devices)
                print("\nAndroid Mongo DB Device IDs: " + Android_MongoDBDeviceID_str)
            else:
                print("\nNo Android Devices found.")

            # iOS Devices Information
            if globalvar.iOS_Devices:
                print("\niOS Devices Information:")
                for device in globalvar.iOS_Devices:
                    print("iOS Mongo DB Device ID:", device[0])
                    print("iOS Device ID:", device[1])
                print("\nExtracted iOS Devices Information")
                iOS_DeviceIDs_str = ', '.join(device[1] for device in globalvar.iOS_Devices)
                print("\niOS Device IDs: " + iOS_DeviceIDs_str)
                iOS_MongoDBDeviceID_str = ', '.join(
                    device[0] for device in globalvar.iOS_Devices)
                print("\niOS Mongo DB Device IDs: " + iOS_MongoDBDeviceID_str)
            else:
                print("\nNo iOS Devices found.")

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
        print(
            "------------- Failed to display all the devices for page size 100 (iOS, Android and Windows) ---------------------------\n\n")
        assert False


# Page Size = 500
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_3002_All_Devices_500 == 0, reason="policy is not opened")
@pytest.mark.positivetest
@pytest.mark.devices
@pytest.mark.regressiontest
@pytest.mark.run(order=30002)
def test_tc_3002_All_Devices_500(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        Devices_PageSize_500 = allDevices(globalvar.page_1, globalvar.page_500)
        apiUrl = globalvar.BaseURL + Devices_PageSize_500
        print("\n\n------------------- All the Devices ---------------------------\n")
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.AllDevices, timeout=globalvar.timeout)
        curl_str1 = Utils.getCurlEquivalent(res)
        print(curl_str1)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
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
        print(
            "------------- Failed to display all the devices for page size 500 (iOS, Android and Windows) ---------------------------\n\n")
        assert False


# Page Size = 1000
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_3003_All_Devices_1000 == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.devices
@pytest.mark.regressiontest
@pytest.mark.run(order=30003)
def test_tc_3003_All_Devices_1000(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        Devices_PageSize_1000 = allDevices(globalvar.page_1, globalvar.page_1000)
        apiUrl = globalvar.BaseURL + Devices_PageSize_1000
        print("\n\n------------------- Device count ---------------------------\n")
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.AllDevices, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            if res.status_code == 200:
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
        print(
            "------------- Failed to display all the devices for page size 1000 (iOS, Android and Windows) ---------------------------\n\n")
        assert False


# # Unenrolled Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3004_Unenrolled_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30004)
# def test_tc_3004_Unenrolled_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         UnenrolledDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + UnenrolledDevices
#         print("\n\n------------------- Unenrolled Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.UnenrolledDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display unenrolled devices ---------------------------\n\n")
#         assert False
#
#
# # Stolen Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3005_Stolen_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30005)
# def test_tc_3005_Stolen_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         StolenDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + StolenDevices
#         print("\n\n------------------- Stolen Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.StolenDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display stolen devices ---------------------------\n\n")
#         assert False
#
#
# # Replaced Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3006_Replaced_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30006)
# def test_tc_3006_Stolen_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         ReplacedDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + ReplacedDevices
#         print("\n\n------------------- Replaced Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.ReplacedDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display replaced devices ---------------------------\n\n")
#         assert False
#
#
# # Active Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3007_Active_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30007)
# def test_tc_3007_Active_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         ActiveDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + ActiveDevices
#         print("\n\n------------------- Active Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.ActiveDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display active devices ---------------------------\n\n")
#         assert False
#
#
# # Lost Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3008_Lost_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30008)
# def test_tc_3008_Lost_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         LostDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + LostDevices
#         print("\n\n------------------- Lost Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.LostDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display lost devices ---------------------------\n\n")
#         assert False
#
#
# # Unprovisioned Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3009_Unprovisioned_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30009)
# def test_tc_3009_Unprovisioned_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         UnprovisionedDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + UnprovisionedDevices
#         print("\n\n------------------- Unprovisioned Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.LostDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display unprovisioned devices ---------------------------\n\n")
#         assert False
#
#
# # Search Policy
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3010_Search_Policy == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30010)
# def test_tc_3010_Search_Policy(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         PolicySearch = searchPolicies(globalvar.page_1, globalvar.page_50000, "Kiosk")
#         apiUrl = globalvar.BaseURL + PolicySearch
#         print("\n\n------------------- Search Policy ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(
#             "------------- Failed to display the search policy ---------------------------\n\n")
#         assert False
#
#
# # Filter By Group Names
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3011_Filter_By_GroupNames == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30011)
# def test_tc_3011_Filter_By_GroupNames(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         FilterByGroupNames = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + FilterByGroupNames
#         print("\n\n------------------- Filter By Group Names ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.FilterByGroupName, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display the Filter By Group Names ---------------------------\n\n")
#         assert False
#
#
# # Enable All Devices State
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3012_Enable_All_DevicesState == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30012)
# def test_tc_3012_EnableAllDevicesState(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         EnableAllDevicesState = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + EnableAllDevicesState
#         print("\n\n------------------- Enable All Devices State ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.EnableAllDevicesState,
#                             timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display all the enabled devices State ---------------------------\n\n")
#         assert False
#
#
# # Disable All Devices State
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3013_Disable_All_DevicesState == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30013)
# def test_tc_3013_DisableAllDevicesState(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         DisableAllDevicesState = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + DisableAllDevicesState
#         print("\n\n------------------- Disable All Devices State ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.DisableAllDevicesState,
#                             timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display all the disabled devices State ---------------------------\n\n")
#         assert False
#
#
# # View by Devices Type
# # Android Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3014_Android_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30014)
# def test_tc_3014_Android_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         AndroidDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + AndroidDevices
#         print("\n\n------------------- Android Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.AndroidDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display all the Android devices ---------------------------\n\n")
#         assert False
#
#
# # iOS Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3015_iOS_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30015)
# def test_tc_3015_iOS_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         iOSDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + iOSDevices
#         print("\n\n------------------- iOS Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.iOSDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display all the iOS devices ---------------------------\n\n")
#         assert False
#
#
# # Windows Devices
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_3016_Windows_Devices == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30016)
# def test_tc_3016_Windows_Devices(url):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WindowsDevices = allDevices(globalvar.page_1, globalvar.page_1000)
#         apiUrl = globalvar.BaseURL + WindowsDevices
#         print("\n\n------------------- Windows Devices ---------------------------\n")
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.WindowsDevices, timeout=globalvar.timeout)
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n" + "200 The request was a success!")
#                 print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             print("\n" + "500 Result not found!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display all the Windows devices ---------------------------\n\n")
#         assert False
