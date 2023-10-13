from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import general_payload as RequestInfo
import itertools


def allDevices(page, size):
    AllDevices = "enterprise/rest/v3/device/all?page={page}&size={size}".format(page=page, size=size)
    return AllDevices


def searchPolicies(page, size, search):
    searchPolicy = "enterprise/rest/v3/policy/all?page={page}&size={size}&search={search}&deviceCount=false".format(
        page=page, size=size, search=search)
    return searchPolicy


# Devices States and Pagination
@pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_3001_All_Devices_Pagination == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.devices
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=30001)
def test_tc_3001_All_Devices_Paginations(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token  Skipping test")
    try:
        apiUrl = globalvar.BaseURL + allDevices(Page, Size)
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
            "------------- Failed to display all the devices for page size 100 (iOS, Android and Windows) ---------------------------\n\n")
        assert False


# # Filter by Device States
# # Updated custom_test_name function
# def custom_test_name(params):
#     Page, Size, provisioned, replaced, lost, stolen, unEnrolled, active = params
#     return f"Page - {Page} - Size - {Size} - Active - {active} - Provisioned - {provisioned} - Replaced - {replaced} - Lost - {lost} - Stolen - {stolen} - Unenrolled - {unEnrolled}"
#
# TrueFalse = [True, False]
#
# # Generate all combinations of True and False for DeviceState keys
# combinations = list(itertools.product(TrueFalse, repeat=6))
#
# # Updated @pytest.mark.parametrize decorator
# @pytest.mark.parametrize(
#     'test_params',
#     [(Page, Size, *combo) for Page in globalvar.page for Size in globalvar.pageSize for combo in combinations],
#     ids=custom_test_name
# )
# def test_tc_3002_Device_States(test_params):
#     Page, Size, provisioned, active, replaced, lost, stolen, unEnrolled = test_params
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#
#     try:
#         apiUrl = globalvar.BaseURL + allDevices(Page, Size)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         device_state = RequestInfo.Base_DeviceState.copy()
#         device_state["provisioned"] = provisioned
#         device_state["replaced"] = replaced
#         device_state["lost"] = lost
#         device_state["stolen"] = stolen
#         device_state["unEnrolled"] = unEnrolled
#         device_state["active"] = active
#
#         res = requests.post(url=apiUrl, headers=Headers, json=device_state, timeout=globalvar.timeout)
#
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             if res.status_code == 200:
#                 print("\n200 The request was a success!")
#                 print(
#                     "\n" + "Request URL: " + apiUrl +
#                     "\n" + "Request Method: " + res.request.method +
#                     "\n" + "Status Code: " + str(res.status_code) +
#                     "\n" + "Request Payload: " + str(device_state) +
#                     "\n" + "Response: " + str(res.content) + "\n")
#                 print(f"DeviceState: {device_state} with Page {Page} and Size {Size}\n")
#         elif res.status_code == 400:
#             print("\n400 Bad Request!\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n404 Result not found!\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n500 Internal Server Error!\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print(f"Request did not succeed! Status code: {res.status_code}")
#             assert False, f"Received {res.status_code} response"
#     except BaseException as e:
#         print(f"Exception: {str(e)}")
#         now2 = datetime.now()
#         print(f"Time taken: {str(now2 - now1)}")
#         print(f"Failed to display the Provisioned: {provisioned}, Active: {active}, Replaced: {replaced}, Lost: {lost}, Stolen: {stolen}, Unenrolled: {unEnrolled}")
#         assert False
#
#
# # Search Policy
# @pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
# @pytest.mark.skipif(Execute.test_tc_3003_Search_Policy == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30003)
# def test_tc_3003_Search_Policy(Page, Size):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         PolicySearch = searchPolicies(Page, Size, "Kiosk")
#         apiUrl = globalvar.BaseURL + PolicySearch
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
#                 print("\n\n------------------- Searched the Policy ---------------------------\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
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
# @pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
# @pytest.mark.skipif(Execute.test_tc_3004_Filter_By_GroupNames == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30004)
# def test_tc_3004_Filter_By_GroupNames(Page, Size):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#             FilterByGroupNames = allDevices(Page, Size)
#             apiUrl = globalvar.BaseURL + FilterByGroupNames
#             print("\n\n------------------- Filter By Group Names ---------------------------\n")
#             Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#             res = requests.post(url=apiUrl, headers=Headers, json=RequestInfo.FilterByGroupName, timeout=globalvar.timeout)
#             if res.status_code == 200:
#                 curl_str1 = Utils.getCurlEquivalent(res)
#                 print(curl_str1)
#                 if res.status_code == 200:
#                     print("\n" + "200 The request was a success!")
#                     print(  # "\n" + "Header: " + str(res.headers) + "\n"
#                         "\n" + "Request URL: " + apiUrl +
#                         "\n" + "Request Method: " + res.request.method +
#                         "\n" + "Status Code: " + str(res.status_code) +
#                         "\n" + "Response: " + str(res.content) + "\n")
#             elif res.status_code == 400:
#                 print("\n" + "400 Bad Request!" + "\n")
#                 print("\n" + "400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n" + "404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n" + "500 Internal Server Error!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print("Request did not succeed! Status code:", res.status_code)
#                 assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print("------------- Failed to display the Filter By Group Names ---------------------------\n\n")
#         assert False
#
# # View by Devices Type
# DeviceTypes = ["ANDROID", "IOS", "WINDOWS"]
#
#
# # Android, iOS, Windows Devices
# @pytest.mark.parametrize('Page, Size, DeviceType',
#                          [(p, s, d) for p in globalvar.page for s in globalvar.pageSize for d in DeviceTypes])
# @pytest.mark.skipif(Execute.test_tc_3005_View_By_Device_Types == 0, reason="skip test")
# @pytest.mark.negativetest
# @pytest.mark.devices
# @pytest.mark.regressiontest
# @pytest.mark.run(order=30005)
# def test_tc_3005_Devices_Types(Page, Size, DeviceType):
#     now1 = datetime.now()
#     if globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvar.BaseURL + allDevices(Page, Size)
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         DevicesTypes = {
#             "search": None,
#             "provisioned": True,
#             "replaced": None,
#             "lost": None,
#             "stolen": None,
#             "unEnrolled": None,
#             "type": DeviceType,  # Set the device type dynamically
#             "active": None,
#             "policyIdList": None
#         }
#         res = requests.post(url=apiUrl, headers=Headers, json=DevicesTypes, timeout=globalvar.timeout)
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
#                 print(f" Page {Page}, Size {Size} and Type {DeviceType}\n")
#         elif res.status_code == 400:
#             print("\n" + "400 Bad Request!" + "\n")
#             # Add your assertions or actions for 400 Bad Request response here
#             assert False, "Received 400 Bad Request response"
#         elif res.status_code == 404:
#             print("\n" + "404 Result not found!" + "\n")
#             # Add your assertions or actions for 404 Not Found response here
#             assert False, "Received 404 response"
#         elif res.status_code == 500:
#             print("\n" + "500 Internal Server Error!" + "\n")
#             # Add your assertions or actions for 500 Internal Server Error response here
#             assert False, "Received 500 response"
#         else:
#             print("Request did not succeed! Status code:", res.status_code)
#             assert False, "Received {res.status_code} response"
#     except BaseException as e:
#         print("Exception : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(f" Failed to display the Page {Page}, Size {Size} and Type {DeviceType}\n")
#         assert False
