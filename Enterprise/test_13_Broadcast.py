import json
from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import general_payload as Request


def POSTMessageHistory(page, pageSize):
    url = f"enterprise/rest/weguard-v2/messageHistory?page={page}&pageSize={pageSize}".format(page=page,
                                                                                              pageSize=pageSize)
    return url


def GETBroadcastPolicies(page, size):
    url = f"enterprise/rest/v3/policy/all?page={page}&size={size}&deviceCount=false&impersonator=false"
    return url


def POSTMessageHistory2(page, pageSize):
    url = f"enterprise/rest/weguard-v2/messageHistory?page={page}&pageSize={pageSize}".format(page=page,
                                                                                              pageSize=pageSize)
    return url


def GETDeviceReadMessage(reqID, page, pageSize):
    url = f"enterprise/rest/weguard-v2/messageHistory/devices/{reqID}?page=1&pageSize=100".format(reqID=reqID,
                                                                                                  page=page,
                                                                                                  pageSize=pageSize)
    return url


FCMUpdate = "enterprise/rest/weguard-v2/fcmUpdate"

BroadcastPolicy = "enterprise/rest/broadcast/policy/multi"

# Rich Text
BroadcastMessageRichText = "enterprise/rest/broadcast/message/save"


# Broadcast - GET Message History
@pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_13001_Broadcast_MessageHistory_Type_GET == 0,
                    reason="GET Broadcast - Message History is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=13001)
def test_tc_13001_Broadcast_Message_History(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token  Skipping test")
    try:
        apiUrl = globalvar.BaseURL + POSTMessageHistory(Page, Size)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        payload = {"actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode,
                   "type": "FCM_MESSAGE"}
        res = requests.post(url=apiUrl, headers=Headers, json=payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(
                # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n")
            print("\nBroadcast Message History with Page={}, Size={}".format(Page, Size))
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
        print("\nFailed to display the broadcast message history with Page={}, Size={}".format(Page, Size))
        assert False


# Broadcast - GET All Policy
@pytest.mark.parametrize('Page, Size', [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_13002_Broadcast_All_Policies_GET == 0,
                    reason="GET Broadcast - All Policies is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=13002)
def test_tc_13002_Broadcast_AllPolicies(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token  Skipping test")
    try:
        apiUrl = globalvar.BaseURL + GETBroadcastPolicies(Page, Size)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(
                # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n")
            print("\nBroadcast message history of all policies with Page={}, Size={}".format(Page, Size))
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
        print("\nFailed to display the broadcast message history of all policies with Page={}, Size={}".format(Page,
                                                                                                               Size))
        assert False


# Broadcast - POST Message History
wcm_values = [True, False]


@pytest.mark.parametrize('Page, Size, WcmValue',
                         [(p, s, w) for p in globalvar.page for s in globalvar.pageSize for w in wcm_values])
@pytest.mark.skipif(Execute.test_tc_13003_Broadcast_MessageHistory_POST == 0,
                    reason="POST Broadcast - Message History is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=13003)
def test_tc_13003_Broadcast_Message_History_POST(Page, Size, WcmValue):
    now1 = datetime.now()
    
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    
    try:
        apiUrl = globalvar.BaseURL + POSTMessageHistory2(Page, Size)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {"actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode, "wcm": WcmValue,
                   "type": "FCM_MESSAGE"}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
                "\n" + "Response: " + str(res.content) + "\n")
            response_data = json.loads(res.content)
            licenses = response_data['entity']['licenses']
            globalvar.BroadcastReqID = []  # Initialize the list before appending 'reqID' values
            for license in licenses:
                req_id = license.get('reqID')
                if req_id is not None:
                    globalvar.BroadcastReqID.append(req_id)
            print("Broadcast Req ID for Message Read by Devices: ", globalvar.BroadcastReqID)
            print("\nMessage History with Page={}, Size={}, WcmValue={}".format(Page, Size, WcmValue))
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
        print("\nFailed to display the Message History with Page={}, Size={}, WcmValue={}".format(Page, Size, WcmValue))
        assert False


# Broadcast - Message Read by Devices
@pytest.mark.parametrize('Page, Size',
                         [(p, s) for p in globalvar.page for s in globalvar.pageSize])
@pytest.mark.skipif(Execute.test_tc_13004_Broadcast_Message_Read_By_Device_GET == 0,
                    reason="GET Broadcast - Message Read by Devices is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=13004)
def test_tc_13004_Broadcast_Message_Read_By_Devices_GET(Page, Size):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        # for broadcastMessageReqID in globalvar.BroadcastReqID:
        apiUrl = globalvar.BaseURL + GETDeviceReadMessage(globalvar.BroadcastReqID[0], Page, Size)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(
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
        print("\nFailed to display the Message Ready By Devices with Page={}, Size={}".format(Page, Size))
        assert False


# Broadcast - Plain Text --> Message to All Level
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13005_Broadcast_Send_Message_Level_All_Plain_Text == 0,
                    reason="Broadcast plain text message to level = All is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13005)
def test_tc_13005_Broadcast_Send_Message_All_Level_Plain_Text(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + FCMUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "topic": globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "FCM_MESSAGE", "isLicenseLevel": True, "actCode": globalvar.activationCode,
            "pActCode": globalvar.productActivationCode,
            "message": "{\"textColor\":\"#ffffff\",\"bgColor\":\"#000000\",\"textType\":\"normal\",\"title\": " + Request.random_title + ",\"iconUrl\":\"https://stage-cache.weguard.ai/qa-cache-weguard-io/64cb86dd80f4b80b1dc65e73/238ed64b982bc5d4274d812d1b354157/5.1.15ITVIRTUsers.png\",\"body\":" + Request.random_message + "}",
            "pId": None, "priority": "high", "id": Request.RandomID, "reqId": Request.UUID}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
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
            "------------- Failed send the plain text broadcast to All level ---------------------------\n\n")
        assert False


# Broadcast - Plain Text --> Message to Group Level
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13006_Broadcast_Send_Message_Level_Group_Plain_Text == 0,
                    reason="Broadcast plain text message to level = Group is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13006)
def test_tc_13006_Broadcast_Send_Message_Group_Level_Plain_Text(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        # for policyName in globalvar.Android_All_Policy_Names:
        #     for policyId in globalvar.Android_All_Policy_IDs:
        apiUrl = globalvar.BaseURL + BroadcastPolicy
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "message": "{\"textColor\":\"#ffffff\",\"bgColor\":\"#000\",\"textType\":\"normal\",\"title\": " + Request.random_title + ",\"body\":" + Request.random_message + "}",
            "policies": [{"WCM": False, "policyName": globalvar.Android_All_Policy_Names[0],
                          "policyId": globalvar.Android_All_Policy_IDs[0],
                          "reqId": Request.UUID}], "id": Request.RandomID, "reqId": Request.UUID}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
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
            "------------- Failed send the plain text broadcast at Group Level ---------------------------\n\n")
        assert False


# Broadcast - Plain Text --> Message to Device Level
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13007_Broadcast_Send_Message_Level_Device_Plain_Text == 0,
                    reason="Broadcast plain text message to level = Device is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13007)
def test_tc_13007_Broadcast_Send_Message_Device_Level_Plain_Text_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        # for Android_DeviceID in globalvar.Android_DeviceIDs:
        #     for policyId in globalvar.Android_All_Policy_IDs:
        apiUrl = globalvar.BaseURL + FCMUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "topic": globalvar.Android_DeviceIDs[
                         0] + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "FCM_MESSAGE", "isLicenseLevel": False,
            "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode,
            "message": "{\"textColor\":\"#ffffff\",\"bgColor\":\"#000000\",\"textType\":\"normal\",\"body\":" + Request.random_message + ",\"title\":" + Request.random_title + "}",
            "pId": globalvar.Android_All_Policy_IDs[0], "priority": "high", "id": Request.RandomID,
            "reqId": Request.UUID}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
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
            "------------- Failed send the plain text broadcast at Device Level ---------------------------\n\n")
        assert False


# Broadcast - Rich Text --> Message to All Level
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13008_Broadcast_Send_Message_Level_All_Rich_Text == 0,
                    reason="Broadcast rich text message to level = All is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13008)
def test_tc_13008_Broadcast_Send_Message_All_Level_Rich_Text_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + BroadcastMessageRichText
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {"textColor": "#ffffff", "bgColor": "#000", "textType": "rich", "title": "Test",
                   "body": "QA&nbsp;<a href=\"https://qa-cloud.weguard.ai/#/login\" target=\"_blank\">https://qa-cloud.weguard.ai/#/login</a>"}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
                "\n" + "Response: " + str(res.content) + "\n")
            response_data = json.loads(res.content)
            entity = response_data['entity']
            globalvar.BroadcastMessageID = []  # Initialize the list before appending 'messageID' values
            if isinstance(entity, dict):
                message_id = entity.get('messageID')
                if message_id is not None:
                    globalvar.BroadcastMessageID.append(message_id)
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
            "------------- Failed send the rich text broadcast to All level ---------------------------\n\n")
        assert False


# Broadcast - Rich Text --> Message to All Level --> FCM Update
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13011_Broadcast_FCMUpdate == 0,
                    reason="Broadcast rich text message to level = All fcmUpdate is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=130011)
def test_tc_130012_Broadcast_Send_Message_All_Level_Rich_Text_POST_FCMUpdate(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + FCMUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "topic": globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "FCM_MESSAGE", "isLicenseLevel": True, "actCode": globalvar.activationCode,
            "pActCode": globalvar.productActivationCode,
            "message": "{\"textColor\":\"#ffffff\",\"bgColor\":\"#000000\",\"textType\":\"rich\",\"title\":\"" + str(
                Request.random_title) + "\",\"iconUrl\":\"https://stage-cache.weguard.ai/qa-cache-weguard-io/64cb86dd80f4b80b1dc65e73/238ed64b982bc5d4274d812d1b354157/5.1.15ITVIRTUsers.png\",\"body\":\"" + str(
                Request.random_message) + "\", \"bMsgBodyRef\":\"" + str(globalvar.BroadcastMessageID) + "\"}",
            "pId": None, "priority": "high", "id": str(Request.RandomID), "reqId": str(Request.UUID)}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
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
            "------------- Failed send the rich text broadcast message to level = All fcm update ---------------------------\n\n")
        assert False


# Broadcast - Rich Text --> Message to Group Level = Save API
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13009_Broadcast_Send_Message_Level_Group_Rich_Text == 0,
                    reason="Broadcast rich text message to level = Group is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13009)
def test_tc_13009_Broadcast_Send_Message_Group_Level_Rich_Text_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + BroadcastMessageRichText
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {"textColor": "#ffffff", "bgColor": "#000", "textType": "rich", "body": "qa", "title": "test"}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
                "\n" + "Response: " + str(res.content) + "\n")
            response_data = json.loads(res.content)
            entity = response_data['entity']
            globalvar.BroadcastMessageID = []  # Initialize the list before appending 'messageID' values
            if isinstance(entity, dict):
                message_id = entity.get('messageID')
                if message_id is not None:
                    globalvar.BroadcastMessageID.append(message_id)
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
            "------------- Failed send the rich text broadcast to Group level ---------------------------\n\n")
        assert False


# Broadcast - Rich Text --> Message to Group Level = Broadcast policy (Multi)
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13009_Broadcast_Send_Message_Level_Group_Rich_Text == 0,
                    reason="Broadcast rich text message to level = Group is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13009)
def test_tc_13009_Broadcast_Send_Message_Group_Level_Rich_Text_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        # for policyName in globalvar.Android_All_Policy_Names:
        #     for policyId in globalvar.Android_All_Policy_IDs:
        apiUrl = globalvar.BaseURL + BroadcastPolicy
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "message": "{\"textColor\":\"#ffffff\",\"bgColor\":\"#000\",\"textType\":\"normal\",\"title\": " + Request.random_title + ",\"body\":" + Request.random_message + "}",
            "policies": [{"WCM": False, "policyName": globalvar.Android_All_Policy_Names[0],
                          "policyId": globalvar.Android_All_Policy_IDs[0],
                          "reqId": Request.UUID}], "id": Request.RandomID, "reqId": Request.UUID}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
                "\n" + "Response: " + str(res.content) + "\n")
            response_data = json.loads(res.content)
            entity = response_data['entity']
            globalvar.BroadcastMessageID = []  # Initialize the list before appending 'messageID' values
            if isinstance(entity, dict):
                message_id = entity.get('messageID')
                if message_id is not None:
                    globalvar.BroadcastMessageID.append(message_id)
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
            "------------- Failed send the rich text broadcast to Group level ---------------------------\n\n")
        assert False


# Broadcast - Plain Text --> Message to Device Level = Save API
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13010_Broadcast_Send_Message_Level_Device_Rich_Text == 0,
                    reason="Broadcast rich text message to level = Device is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13010)
def test_tc_13010_Broadcast_Send_Message_Device_Level_Rich_Text_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        # for Android_DeviceID in globalvar.Android_DeviceIDs:
        #     for policyId in globalvar.Android_All_Policy_IDs:
        apiUrl = globalvar.BaseURL + BroadcastMessageRichText
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "textColor": "#ffffff",
            "bgColor": "#000",
            "textType": "rich",
            "body": Request.random_message + "<a href=\"https://www.weguard.com\" target=\"_blank\">WeGuard</a>",
            "title": Request.random_title
        }
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
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
            "------------- Failed send the rich text broadcast at Device Level ---------------------------\n\n")
        assert False


# Broadcast - Rich Text --> Message to Device Level = FCM Update
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_13011_Broadcast_FCMUpdate == 0,
                    reason="Broadcast rich text message to level = Device is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.run(order=13007)
def test_tc_13011_Broadcast_FCMUpdate_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        # for Android_DeviceID in globalvar.Android_DeviceIDs:
        #     for policyId in globalvar.Android_All_Policy_IDs:
        apiUrl = globalvar.BaseURL + FCMUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Payload = {
            "topic": globalvar.Android_DeviceIDs[
                         0] + "_" + globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "FCM_MESSAGE", "isLicenseLevel": False,
            "actCode": globalvar.activationCode, "pActCode": globalvar.productActivationCode,
            "message": "{\"textColor\":\"#ffffff\",\"bgColor\":\"#000000\",\"textType\":\"normal\",\"body\":" + Request.random_message + ",\"title\":" + Request.random_title + ", \"bMsgBodyRef\":\"" + str(
                globalvar.BroadcastMessageID) + "\"}",
            "pId": globalvar.Android_All_Policy_IDs[0],
            "priority": "high", "id": Request.RandomID, "reqId": Request.UUID}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(  # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(Payload) +
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
            "------------- Failed send the plain text broadcast at Device Level ---------------------------\n\n")
        assert False
