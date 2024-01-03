# import json
# from datetime import datetime
# import pytest
# import requests
# import globalvariables as globalvar
# import Executor as Execute
# import test_GETutils as Utils
# import general_payload as GeneralPayload
#
# # Constants
# GenericCSP = "windows/rest/csp/genericcsp"
# JSON_File_Path = "/Users/chakrapani/AIWeGuardAPIs/Windows_Advanced_Settings/CSP.json"
#
# # Load CSPs JSON data
# with open(JSON_File_Path, 'r') as json_file:
#     try:
#         CSP_Data = json.load(json_file)
#     except json.JSONDecodeError as e:
#         print(f"JSON parsing error: {e}")
#
#
# # Define the CSPData class (customize according to your data structure)
# class CSPData:
#     def __init__(self, omauri, csp, category, name, description, dataType, allowedActions, supportedValues,
#                  supportedVersions, enabled):
#         self.omauri = omauri
#         self.csp = csp
#         self.category = category
#         self.name = name
#         self.description = description
#         self.dataType = dataType
#         self.allowedActions = allowedActions
#         self.supportedValues = supportedValues
#         self.supportedVersions = supportedVersions
#         self.enabled = enabled
#
#
# # Create a list to store CSP objects
# csp_objects = []
#
# test_data = []
#
# # Iterate through CSPs in the order they appear in the JSON file
# for csp_obj_data in CSP_Data:
#     # Create a CSPData object
#     csp_obj = CSPData(
#         csp_obj_data["omauri"],
#         csp_obj_data["csp"],
#         csp_obj_data["category"],
#         csp_obj_data["name"],
#         csp_obj_data["description"],
#         csp_obj_data["dataType"],
#         csp_obj_data["allowedActions"],
#         csp_obj_data["supportedValues"],
#         csp_obj_data["supportedVersions"],
#         csp_obj_data["enabled"]
#     )
#     csp_objects.append(csp_obj)
#     print(f"Added CSP object: {csp_obj.name}")
#
# # Inside the loop where you iterate through CSP objects
# for csp_obj in csp_objects:
#     allowed_actions = [
#         action for action, allowed in csp_obj.allowedActions.items() if
#         isinstance(allowed, bool) and allowed
#     ]
#     GeneralPayload.Allowed_Actions[csp_obj.omauri] = allowed_actions
#
#     # Extract supported values
#     supported_values = csp_obj.supportedValues.get("allowedValues")
#     if supported_values is not None:
#         supported_values_list = supported_values.split(",")
#     else:
#         supported_values_list = []
#
#     # If 'allowedValues' is not present, calculate min and max from supported values
#     # If 'allowedValues' is not present, calculate min and max from supported values
#     if not supported_values_list:
#         supported_values_list = csp_obj.supportedValues.get("supportedValues", "").split(",")
#         # Filter out non-integer values and empty strings
#         supported_values_list = [value for value in supported_values_list if value.isdigit()]
#         supported_values_list = [int(value) for value in supported_values_list]  # Convert to integers
#
#     if supported_values_list:
#         min_value = min(supported_values_list)
#         max_value = max(supported_values_list)
#     else:
#         min_value = max_value = 0
#
#     # Print "min" and "max" values
#     print(f"OMA-URI: {csp_obj.omauri}, Min Value: {min_value}, Max Value: {max_value}")
#
#     # Include actions where "allowedActions" is set to true
#     for action in ["get", "add", "replace", "delete", "exec"]:
#         if action in allowed_actions:
#             # If it's "get," exclude "value" from the payload
#             if action == "get":
#                 test_data.append((csp_obj, action, None))
#             else:
#                 for value in supported_values_list:
#                     test_data.append((csp_obj, action, value))
#
# # Define a function to format the test case name
# def format_test_case_name(data, action, value):
#     if action == "get":
#         return f"OMA-URI: {data.omauri}, Action: {action}, Supported Values: None"
#     return f"OMA-URI: {data.omauri}, Action: {action}, Supported Values: {value}"
#
#
# # Execute actions based on allowedActions and values
# @pytest.mark.parametrize('data, action, value', test_data,
#                          ids=[format_test_case_name(data, action, value) for data, action, value in test_data])
# @pytest.mark.skipif(Execute.test_tc_1170001_Windows_Generic_CSPs_POST == 0, reason="Windows CSP is skipped")
# @pytest.mark.positivetest
# @pytest.mark.WindowsDevice
# @pytest.mark.regressiontest
# @pytest.mark.run(order=1170001)
# def test_Windows_CSPs(data, action, value):
#     print(f"Received data: {data.omauri}, action: {action}, value: {value}")
#     now1 = datetime.now()
#     oma_uri = data.omauri
#     dataType = data.dataType
#     policy_id = globalvar.Windows_Policy_IDs[0]  # Make sure you have this defined correctly
#
#     try:
#         apiUrl = globalvar.BaseURL + GenericCSP
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#
#         # Create the payload
#         payload = {"csps": [{"omauri": oma_uri, "dataType": dataType, "action": action, "value": value}],
#                    "policyId": policy_id}
#
#         # Exclude "value" from payload for "get" actions
#         if action == "get":
#             del payload["csps"][0]["value"]
#
#         res = requests.post(url=apiUrl, headers=Headers, json=payload, timeout=globalvar.timeout)
#
#         # Print supported values and allowed actions for each CSP
#         print(f"\nOMA-URI: {oma_uri}\n")
#         print(f"Supported Values: {', '.join(supported_values)}\n")
#         print(f"Min Value: {min_value}, Max Value: {max_value}\n")
#         print(f"Allowed Actions: {', '.join(GeneralPayload.Allowed_Actions.get(oma_uri, []))}\n")
#
#         if res.status_code == 200:
#             curl_str1 = Utils.getCurlEquivalent(res)
#             print(curl_str1)
#             print("\n200 The request was a success!")
#             print(
#                 "\n" + "Request URL: " + apiUrl +
#                 "\n" + "Request Method: " + res.request.method +
#                 "\n" + "Status Code: " + str(res.status_code) +
#                 "\n" + "Request Payload: " + str(payload) +
#                 "\n" + "Response: " + str(res.content) + "\n")
#             print(f"Executed test for OMA-URI: {oma_uri}, Action: {action}, Value: {value}")
#         else:
#             print(f"Request did not succeed! Status code: {res.status_code}")
#             # Handle different status codes here as needed
#             if res.status_code == 400:
#                 print("\n400 Bad Request!" + "\n")
#                 # Add your assertions or actions for 400 Bad Request response here
#                 assert False, "Received 400 Bad Request response"
#             elif res.status_code == 404:
#                 print("\n404 Result not found!" + "\n")
#                 # Add your assertions or actions for 404 Not Found response here
#                 assert False, "Received 404 response"
#             elif res.status_code == 500:
#                 print("\n500 Result not found!" + "\n")
#                 # Add your assertions or actions for 500 Internal Server Error response here
#                 assert False, "Received 500 response"
#             else:
#                 print(f"Request did not succeed! Status code: {res.status_code}")
#                 # Handle other status codes here as needed
#                 assert False, f"Received {res.status_code} response"
#     except Exception as e:
#         print("RequestException : " + str(e))
#         now2 = datetime.now()
#         print("Time taken: " + str(now2 - now1))
#         print(f"Failed to execute the test for OMA-URI: {oma_uri}, Action: {action}, Value: {value}")
