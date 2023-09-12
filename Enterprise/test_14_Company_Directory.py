from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import WeGuardLogger as WeGuard
import general_payload as GeneralPayload


def POSTAccountLevelContacts(page, size):
    return "enterprise/rest/contacts/all?page={page}&size={size}".format(page=page, size=size)


def Delete_Account_and_Policy_Level_Contacts(ContactsMongoDBId):
    return "enterprise/rest/contacts/{ContactsMongoDBId}".format(ContactsMongoDBId=ContactsMongoDBId)


def POSTPolicyLevelContacts(policyId, pageSize, page):
    return "enterprise/rest/weguard-v2/devices/forgroup/{policyId}?pageSize={pageSize}&page={page}".format(
        policyId=policyId, pageSize=pageSize, page=page)


fcmUpdate = "enterprise/rest/weguard-v2/fcmUpdate"


# Account Level Contacts
# Account Level: POST method to create contacts on the portal
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14000_Create_Contacts_Account_Level_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14000)
def test_tc_14000_Company_Directory_Create_Contacts_Account_Level_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + fcmUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        CreateContactAccountLevel = [
            {"firstName": GeneralPayload.firstName, "lastName": GeneralPayload.lastName,
             "displayName": GeneralPayload.displayName, "nickName": GeneralPayload.nickName,
             "companyName": GeneralPayload.companyName, "jobTitle": GeneralPayload.jobTitle,
             "website": GeneralPayload.website, "notes": GeneralPayload.notes,
             "emailAddresses": GeneralPayload.emailAddresses,
             "phoneNums": GeneralPayload.phoneNums, "postalAddresses": GeneralPayload.postalAddresses,
             "accountId": globalvar.accountId,
             "policyId": None}]
        res = requests.post(url=apiUrl, headers=Headers, json=CreateContactAccountLevel,
                            timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to create the contacts at the Account Level ---------------------------\n\n")
        assert False
        
# Policy Level: POST method to sync contacts on the devices through FCM Update after creating/adding accounts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14001_Contacts_Account_Level_FCM_UPDATE_After_CreatingAdding_Contacts_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14001)
def test_tc_14001_Company_Directory_Contacts_Account_Level_FCM_UPDATE_After_CreatingORAdding_Contacts_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + fcmUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        FCMUpdateAfterDeleteContacts_AccountLevel = {
            "topic": globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "SYNC_CONTACTS", "isLicenseLevel": True,
            "actCode": globalvar.activationCode,
            "pActCode": globalvar.productActivationCode, "message": None, "id": GeneralPayload.RandomContactsIDs}
        res = requests.post(url=apiUrl, headers=Headers, json=FCMUpdateAfterDeleteContacts_AccountLevel,
                            timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to update the fcm at the Account Level after creating/adding the contacts ---------------------------\n\n")
        assert False


# POST method to get all the account level contacts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14002_Contacts_Account_Level_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14002)
def test_tc_14002_Company_Directory_Account_Level_Contacts_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + POSTAccountLevelContacts(globalvar.page_1, globalvar.page_1000)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        Contacts_AccountLevel = {"accountId": globalvar.accountId, "searchText": None}
        res = requests.post(url=apiUrl, headers=Headers, json=Contacts_AccountLevel, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
                  "\n" + "Request URL: " + apiUrl +
                  "\n" + "Request Method: " + res.request.method +
                  "\n" + "Status Code: " + str(res.status_code) +
                  "\n" + "Response: " + str(res.content) + "\n")
            json_resp = res.json()
            # Store profiles based on platform and type
            contact_ids = []  # Create an empty list to store contact IDs
            for contact in json_resp.get('list', []):
                contacts_id = contact.get('id')
                contact_ids.append(contacts_id)  # Append each ID to the list
            globalvar.AccountLevel_Contacts_IDS = contact_ids  # Assign the list to the global variable
            print("Account Level Contacts IDS:", globalvar.AccountLevel_Contacts_IDS)
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
        WeGuard.logger.error(
            "-------------------------- Failed to display the Account Level Contacts ---------------------------\n\n")
        assert False


# DELETE method to delete all the account level contacts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14003_Contacts_Account_Level_DELETE == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14003)
def test_tc_14003_Company_Directory_Contacts_Account_Level_DELETE(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for MongoDB_Contacts_ID in globalvar.AccountLevel_Contacts_IDS:
            apiUrl = globalvar.BaseURL + Delete_Account_and_Policy_Level_Contacts(MongoDB_Contacts_ID)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.delete(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            if res.status_code == 200:
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to delete the Account Level Contacts ---------------------------\n\n")
        assert False


# Account Level: POST method to sync contacts on the devices through FCM Update after executing the "DELETE" API
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14004_Contacts_Account_Level_FCM_UPDATE_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14004)
def test_tc_14004_Company_Directory_Contacts_Account_Level_FCM_UPDATE_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + fcmUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        FCMUpdateAfterDeleteContacts_AccountLevel = {
            "topic": globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "SYNC_CONTACTS", "isLicenseLevel": True,
            "actCode": globalvar.activationCode,
            "pActCode": globalvar.productActivationCode, "message": None, "id": GeneralPayload.RandomContactsIDs}
        res = requests.post(url=apiUrl, headers=Headers, json=FCMUpdateAfterDeleteContacts_AccountLevel,
                            timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to update the fcm at the Account Level Contacts ---------------------------\n\n")
        assert False


# Policy Level Contacts
# Account Level: POST method to create contacts on the portal
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14005_Create_Contacts_Policy_Level_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14005)
def test_tc_14005_Company_Directory_Create_Contacts_Policy_Level_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for policy_ids in globalvar.Android_profile_ids:
            apiUrl = globalvar.BaseURL + fcmUpdate
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            CreateContactPolicyLevel = [
                {"firstName": GeneralPayload.firstName, "lastName": GeneralPayload.lastName,
                 "displayName": GeneralPayload.displayName, "nickName": GeneralPayload.nickName,
                 "companyName": GeneralPayload.companyName, "jobTitle": GeneralPayload.jobTitle,
                 "website": GeneralPayload.website, "notes": GeneralPayload.notes,
                 "emailAddresses": GeneralPayload.emailAddresses,
                 "phoneNums": GeneralPayload.phoneNums, "postalAddresses": GeneralPayload.postalAddresses,
                 "accountId": globalvar.accountId,
                 "policyId": policy_ids}]
            res = requests.post(url=apiUrl, headers=Headers, json=CreateContactPolicyLevel,
                                timeout=globalvar.timeout)
            if res.status_code == 200:
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to create the contacts at the Policy Level ---------------------------\n\n")
        assert False
        
# Account Level: POST method to sync contacts on the devices through FCM Update after creating/adding accounts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14006_Contacts_Account_Level_FCM_UPDATE_After_CreatingAdding_Contacts_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14006)
def test_tc_14006_Company_Directory_Contacts_Account_Level_FCM_UPDATE_After_CreatingORAdding_Contacts_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + fcmUpdate
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        FCMUpdateAfterDeleteContacts_AccountLevel = {
            "topic": globalvar.activationCode + "_" + globalvar.productActivationCode,
            "type": "SYNC_CONTACTS", "isLicenseLevel": True,
            "actCode": globalvar.activationCode,
            "pActCode": globalvar.productActivationCode, "message": None, "id": GeneralPayload.RandomContactsIDs}
        res = requests.post(url=apiUrl, headers=Headers, json=FCMUpdateAfterDeleteContacts_AccountLevel,
                            timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n" + "200 The request was a success!")
            print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to update the fcm at the Account Level after creating/adding the contacts ---------------------------\n\n")
        assert False

# POST method to get all the policy level contacts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14007_Contacts_Policy_Level_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14007)
def test_tc_14007_Company_Directory_Policy_Level_Contacts_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for policyId in globalvar.Android_profile_ids:
            apiUrl = globalvar.BaseURL + POSTPolicyLevelContacts(policyId, globalvar.page_1000, globalvar.page_1)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            if res.status_code == 200:
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Response: " + str(res.content) + "\n")
                json_resp = res.json()
                # Store profiles based on platform and type
                contact_ids = []  # Create an empty list to store contact IDs
                for contact in json_resp.get('list', []):
                    contacts_id = contact.get('id')
                    contact_ids.append(contacts_id)  # Append each ID to the list
                globalvar.PolicyLevel_Contacts_IDS = contact_ids  # Assign the list to the global variable
                print("Account Level Contacts IDS:", globalvar.PolicyLevel_Contacts_IDS)
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
        WeGuard.logger.error(
            "-------------------------- Failed to display the Policy Level Contacts ---------------------------\n\n")
        assert False


# DELETE method to delete all the policy level contacts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14008_Contacts_Policy_Level_DELETE == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14008)
def test_tc_14008_Company_Directory_Contacts_Policy_Level_DELETE(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for MongoDB_Contacts_ID in globalvar.PolicyLevel_Contacts_IDS:
            apiUrl = globalvar.BaseURL + Delete_Account_and_Policy_Level_Contacts(MongoDB_Contacts_ID)
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.delete(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
            if res.status_code == 200:
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to delete the Policy Level Contacts ---------------------------\n\n")
        assert False


# Policy Level: POST method to sync contacts on the devices through FCM Update after executing the "DELETE" API
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14009_Contacts_Policy_Level_FCM_UPDATE_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14009)
def test_tc_14009_Company_Directory_Contacts_Policy_Level_FCM_UPDATE_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for policy_ids in globalvar.Android_profile_ids:
            apiUrl = globalvar.BaseURL + fcmUpdate
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            FCMUpdateAfterDeleteContacts_PolicyLevel = {"topic": policy_ids, "type": "SYNC_CONTACTS",
                                                        "isLicenseLevel": True, "actCode": "9LX20",
                                                        "pActCode": "A1EX-VDFA3",
                                                        "message": None, "id": GeneralPayload.RandomContactsIDs}
            res = requests.post(url=apiUrl, headers=Headers, json=FCMUpdateAfterDeleteContacts_PolicyLevel,
                                timeout=globalvar.timeout)
            if res.status_code == 200:
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
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
        WeGuard.logger.error(
            "-------------------------- Failed to update the fcm at the Policy Level Contacts ---------------------------\n\n")
        assert False
