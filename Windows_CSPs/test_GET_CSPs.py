import json
from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils

GenericCSP = "windows/rest/csp/genericcsp"

# Load the JSON data
with open('/Users/chakrapani/AIWeGuardAPIs/Windows_CSPs/CSPs.json', 'r') as json_file:
    data = json.load(json_file)
    
    # Iterate through each entry in the JSON data
    for entry in data:
        globalvar.OMA_URIs.append(entry["omauri"])
        globalvar.dataType.append(entry['dataType'])
        action = entry.get("action", "get")
        globalvar.Actions.append(action)


# GET CSPs
@pytest.mark.parametrize('oma_uri, dataType, action', zip(globalvar.OMA_URIs, globalvar.dataType, globalvar.Actions))
@pytest.mark.skipif(Execute.test_tc_1170001_Windows_Generic_CSPs_POST == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=1170001)
def test_OMA_URIs(oma_uri, dataType, action):
    now1 = datetime.now()
    if action == "get":  # Check if the action is "get"
        try:
            apiUrl = globalvar.BaseURL + GenericCSP
            Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            policy_id = globalvar.Windows_Policy_IDs[0]
            payload = {"csps": [{"oma-uri": oma_uri, "dataType": dataType, "action": action}], "policyId": policy_id}
            res = requests.post(url=apiUrl, headers=Headers, json=payload, timeout=globalvar.timeout)
            if res.status_code == 200:
                curl_str1 = Utils.getCurlEquivalent(res)
                print(curl_str1)
                print("\n" + "200 The request was a success!")
                print("\n" + "Header: " + str(res.headers) +
                      "\n" + "Request URL: " + apiUrl +
                      "\n" + "Request Method: " + res.request.method +
                      "\n" + "Status Code: " + str(res.status_code) +
                      "\n" + "Request Payload: " + str(payload) +
                      "\n" + "Response: " + str(res.content) + "\n")
                print(f"Executed test for OMA-URI: {oma_uri}")
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
                assert False, f"Received {res.status_code} response"
        except Exception as e:
            print("RequestException : " + str(e))
            now2 = datetime.now()
            print("Time taken: " + str(now2 - now1))
            print(f"Failed to execute the test for OMA-URI: {oma_uri}")
            assert False
