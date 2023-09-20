import json
from datetime import datetime
import pytest
import requests
import globalvariables as globalvar
import Executor as Execute
import test_GETutils as Utils

GenericCSP = "windows/rest/csp/genericcsp"

# Load CSPs JSON data
with open('Windows_Advanced_Settings/CSPs.json', 'r') as json_file:
    csp_data = json.load(json_file)

# Modify the test_data list comprehension to include all combinations of data, action, and value
test_data = []

for entry in csp_data:
    allowed_actions = [action for action, allowed in entry["allowedActions"].items() if allowed.lower() == "true"]
    supported_values = entry["supportedValues"]["allowedValues"].split(",")
    
    # Include "get" action without supported values
    if "get" in allowed_actions:
        test_data.append((entry, "get", None))
    
    # Include "add," "replace," and "delete" actions for supported values
    for action in ["add", "replace", "delete"]:
        if action in allowed_actions:
            for value in supported_values:
                test_data.append((entry, action, value))


# Define a function to format the test case name
def format_test_case_name(data, action, value):
    if action == "get":
        return f"OMA-URI: {data['omauri']}, Action: {action}, Supported Values: None"
    return f"OMA-URI: {data['omauri']}, Action: {action}, Supported Values: {value}"


# Execute actions based on allowedActions and values
@pytest.mark.parametrize('data, action, value', test_data,
                         ids=[format_test_case_name(data, action, value) for data, action, value in test_data])
@pytest.mark.skipif(Execute.test_tc_1170001_Windows_Generic_CSPs_POST == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.WindowsDevice
@pytest.mark.regressiontest
@pytest.mark.run(order=1170001)
def test_Windows_CSPs(data, action, value):
    now1 = datetime.now()
    oma_uri = data["omauri"]
    dataType = data["dataType"]
    policy_id = globalvar.Windows_Policy_IDs[0]  # Make sure you have this defined somewhere
    
    try:
        apiUrl = globalvar.BaseURL + GenericCSP
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        
        # Create the payload
        payload = {"csps": [{"omauri": oma_uri, "dataType": dataType, "action": action, "value": value}],
                   "policyId": policy_id}
        
        # Exclude "value" from payload for "get" actions
        if action == "get":
            del payload["csps"][0]["value"]
        
        res = requests.post(url=apiUrl, headers=Headers, json=payload, timeout=globalvar.timeout)
        if res.status_code == 200:
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print("\n200 The request was a success!")
            print(
                # "\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Request Payload: " + str(payload) +
                "\n" + "Response: " + str(res.content) + "\n")
            print(f"Executed test for OMA-URI: {oma_uri}, Action: {action}, Value: {value}")
        else:
            print(f"Request did not succeed! Status code: {res.status_code}")
            # Handle different status codes here as needed
            if res.status_code == 400:
                print("\n400 Bad Request!" + "\n")
                # Add your assertions or actions for 400 Bad Request response here
                assert False, "Received 400 Bad Request response"
            elif res.status_code == 404:
                print("\n404 Result not found!" + "\n")
                # Add your assertions or actions for 404 Not Found response here
                assert False, "Received 404 response"
            elif res.status_code == 500:
                print("\n500 Result not found!" + "\n")
                # Add your assertions or actions for 500 Internal Server Error response here
                assert False, "Received 500 response"
            else:
                print(f"Request did not succeed! Status code: {res.status_code}")
                # Handle other status codes here as needed
                assert False, f"Received {res.status_code} response"
    except Exception as e:
        print("RequestException : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print(f"Failed to execute the test for OMA-URI: {oma_uri}, Action: {action}, Value: {value}")
        assert False
