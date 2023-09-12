from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils
import WeGuardLogger as WeGuard
import general_payload as Payload

def AccountLevelContacts(page, size):
    return "enterprise/rest/contacts/all?page={page}&size={size}".format(page=page, size=size)

# POST method to get all the account level contacts
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_14001_Contacts_Account_Level_POST == 0, reason="skip test")
@pytest.mark.poitivetest
@pytest.mark.contacts
@pytest.mark.regressiontest
@pytest.mark.run(order=14001)
def test_tc_14001_Company_Directory_Account_Level_Contacts_POST(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + AccountLevelContacts(globalvar.page_1, globalvar.page_1000)
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=Payload.Contacts_AccountLevel, timeout=globalvar.timeout)
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
        WeGuard.logger.error("-------------------------- Failed to display the Account Level Contacts ---------------------------\n\n")
        assert False